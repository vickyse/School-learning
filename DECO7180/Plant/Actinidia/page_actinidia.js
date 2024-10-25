$(document).ready(function () {
    let url = 'https://apps.des.qld.gov.au/species/?op=getspeciesinformation&taxonid=36538';
    $.ajax({
      url: url,
      dataType: 'json', // Modified according to the actual situation
      success: function (data) {
        item = data.Species
        $('#KingdomName').html(item.KingdomName)
        $('#ClassName').html(item.ClassName)
        $('#ClassCommonName').html(item.ClassCommonName)
        $('#PestStatus').html(item.PestStatus)
      },
      error: function () {
        console.error('Failed to load data from the website.');
      }
    });
  })


  // Define two variables to receive two fixed plant data
  var plantList0, plantList1, plantList2
  // Total number of 1st listings, total number of 2nd listings
  var plantNum0, plantNum1, plantNum2
  // Index of the first data currently displayed in the first list, 
  // index of the first data currently displayed in the second list
  var index0 = 0, index1 = 0
  // All data being loaded on the page
  // This variable must be loaded when the initialization of the page is complete,
  // otherwise there may be errors at runtime sometimes
  var lists = new Array()

  // Processing after the document is loaded
  $(document).ready(function () {
    // Handling of content changes in the search text box
    $('#search_input').on('input', function () {
      let word = $('#search_input').val()
      if (word == "") {
        // Hide Query Panel
        $('.search-dropdown-container').hide();
      } else {
        const dropdownContainer = document.querySelector('.search-dropdown-container');
        const dropdownItems = Array.from(dropdownContainer.children);
        // Display query panel with query filtering
        $('.search-dropdown-container').show();
        // Check if there is data, and execute the operation only when there is data
        let flag = false; // Whether there are query results that satisfy the condition, default is false
        $.each(dropdownItems, (index, item) => { // Processing with lambda expressions
          if (item.textContent.toLowerCase().includes(word.toLowerCase())) {
            item.style.display = 'block';
            flag = true;
          } else {
            item.style.display = 'none';
          }
        })
        if (!flag) { // When there are no results, display the no results prompt
          $('#noResult').css('display', 'block');
        } else {
          $('#noResult').css('display', 'none');
        }
      }
    })

    // Call a customized callback function to load the data in top-to-bottom order
    loadDataSequentially();
  });

  // In order to ensure the security of data loading,
  // the data is loaded sequentially using the following callback function method
  // - Start
  // Define a function to load the data
  function loadData(url, callback) {
    $.ajax({
      url: url,
      dataType: 'json', // Modified according to the actual situation
      success: function (data) {
        // The loaded data is handled here, e.g. by storing it in a global variable
        // ...

        // Calling Callback Functions
        callback(data);
      },
      error: function () {
        console.error('Failed to load data from the website.');
      }
    });
  }

  // Define a function to load n types of data in order
  // Here the default is 3, if you want to add types, just add sites directly after the array
  let indexRow = 0   // current line
  function loadDataSequentially() {
    var urls = ['https://apps.des.qld.gov.au/species/?op=getspecies&family=achariaceae', // Family 1
      'https://apps.des.qld.gov.au/species/?op=getspecies&family=acrobolbaceae', // Family 2
      'https://apps.des.qld.gov.au/species/?op=getspecies&family=actinidiaceae']; // Family 3
    var data = []; // Used to store loaded data

    function loadNextData() {
      if (urls.length > 0) {
        var url = urls.shift(); // Get the first URL
        loadData(url, function (data) {
          // Storing loaded data into global variables
          listCur = data.Species;
          if (lists.length == 0) {
            lists = listCur;
          } else {
            $.merge(lists, listCur);
          }

          // Displays the data to the area in the corresponding row
          // Display 4 records per line
          for (let i = 0; i < 4; i++) {
            let item = listCur[i]
            $("#row" + indexRow + "-name" + i).html(item.ScientificName);
            $('#btn-pre' + indexRow).hide();   // Hide the forward button in the corresponding row
          }

          // Assigns a value to the list of data in the corresponding row 
          // and the total number of data according to the current row.
          if (indexRow == 0) {
            plantList0 = listCur;
            plantNum0 = plantList0.length;
          } else if (indexRow == 1) {
            plantList1 = listCur;
            plantNum1 = plantList1.length;
          } else if (indexRow == 2) {
            plantList2 = listCur;
            plantNum2 = plantList2.length;
          }

          indexRow++;
          // Calling the next callback function
          loadNextData();
        });
      } else {
        // All data is loaded, you can use the loaded data here
        initResultDb(); // Populate the query results panel with content based on the loaded data
      }
    }

    // Start loading data sequentially
    loadNextData();
  }

  // Populate the query results panel with content based on the loaded data
  function initResultDb() {
    let strHtml = ''
    $.each(lists, function (index, item) {
      // With a clear destination address, add it to the href here
      if (item.ScientificName == "Acrobolbus") {
        strHtml += '<a class="search-dropdown-item" style="display:none;" href="../detailedpage_Acrobolbus/page.html">' + item.ScientificName + '</a>'
      } else if (item.ScientificName == "Actinidia chinensis") {
        strHtml += '<a class="search-dropdown-item" style="display:none;" href="../detailedpage_Actinidia chinensis/page.html">' + item.ScientificName + '</a>'
      } else if (item.ScientificName == "Baileyoxylon") {
        strHtml += '<a class="search-dropdown-item" style="display:none;" href="../detailedpage_Baileyoxylon/page.html">' + item.ScientificName + '</a>'
      } else if (item.ScientificName == "Goebelobryum grossitextum") {
        strHtml += '<a class="search-dropdown-item" style="display:none;" href="../detailedpage_Goe/page.html">' + item.ScientificName + '</a>'
      } else if (item.ScientificName == "Hydnocarpus") {
        strHtml += '<a class="search-dropdown-item" style="display:none;" href="../detailedpage_Hyd/page.html">' + item.ScientificName + '</a>'
      } else {   // No connection is created if the condition is not met
        strHtml += '<a class="search-dropdown-item" style="display:none;" href="javascript:void(0);">' + item.ScientificName + '</a>'
      }
    })
    strHtml += '<a class="search-dropdown-item" id="noResult" style="display:none;" href="javascript:void(0);">no result</a>'
    $('.search-dropdown-container').html(strHtml)
  }
    // To ensure the security of data loading, 
    // use the following callback function method to load data sequentially
    // - End
