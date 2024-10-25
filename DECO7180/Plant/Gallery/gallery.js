    // Define two variables to receive two fixed plant data
    var plantList0, plantList1, plantList2
    // Total number of 1st listings, total number of 2nd listings
    var plantNum0, plantNum1, plantNum2
    // Index of the first data currently displayed in the first list, 
    // index of the first data currently displayed in the second list
    var index0 = 0, index1 = 0
    // All data being loaded on the page
    // This variable must be loaded when the initialization of the page is complete,
    // otherwise the runtime may sometimes throw an error
    var lists = new Array()
  
    // Processing after the document is loaded
    $(document).ready(function(){
    
      // Handling of content changes in the search text box
      $('#search_input').on('input', function() {
        let word = $('#search_input').val()
        if (word=="") {
          // Hide Query Panel
          $('.search-dropdown-container').hide();
        } else {
          const dropdownContainer = document.querySelector('.search-dropdown-container');
          const dropdownItems = Array.from(dropdownContainer.children);
          // Display query panel with query filtering
          $('.search-dropdown-container').show();
          // Check if there is data and execute the operation only if there is data
          let flag = false; // Whether there are query results that satisfy the condition, default is false
          $.each(dropdownItems, (index, item)=>{ // Processing with lambda expressions
            if (item.textContent.toLowerCase().includes(word.toLowerCase())) {
              item.style.display='block';
              flag = true;
            } else {
              item.style.display='none';
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
  
      // Click event handling for the search button in the search box
      $('#btn-search').click(function(event) {
         // Check if there is data, and execute the operation only when there is data
      })
  
      // Row 1 forward button click event handling
      $('#btn-pre0').click(function(event) {
         showPre(0);   // Show forward operation on line 0
      })
      // Row 1 Backward button click event handling
      $('#btn-next0').click(function(event) {
         showNext(0);   // Show forward operation on line 0
      })
      
      // Line 2 forward button click event handling
      $('#btn-pre1').click(function(event) {
         showPre(1);   // Show forward operation on line 0
      })
  
      // Row 2 Backward button click event handling
      $('#btn-next1').click(function(event) {
         showNext(1);   // Show forward operation on line 0
      })
    });
  
    // To ensure the security of data loading,
    // use the following callback function method to load the data sequentially
    // - Start
    // Define a function to load the data
    function loadData(url, callback) {
      $.ajax({
        url: url,
        dataType: 'json', // Modified according to the actual situation
        success: function(data) {
          // The loaded data is handled here, e.g. by storing it in a global variable
          // ...
  
          // Calling Callback Functions
          callback(data);
        },
        error: function() {
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
          'https://apps.des.qld.gov.au/species/?op=getspecies&family=actinidiaceae' ]; // Family 3
      var data = []; // Used to store loaded data
  
      function loadNextData() {
        if (urls.length > 0) {
          var url = urls.shift(); // Get the first URL
          loadData(url, function(data) {
            // Storing loaded data into global variables
            listCur = data.Species;
            if (lists.length == 0) {
              lists = listCur;
            } else {
              $.merge(lists, listCur);
            }
  
            // Displays the data to the area in the corresponding row
            // Display 4 records per line
            for(let i=0; i<4; i++) {
              let item = listCur[i]
              $("#row"+indexRow+"-name"+i).html(item.ScientificName);
              chgImg(indexRow, i, item.ScientificName); // Change Image
              $('#btn-pre'+indexRow).hide(); // Hide the forward button in the corresponding row
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
          initResultDb(); // Populate the query results panel with content based on the loaded data
        }
      }
  
      // Start loading data sequentially
      loadNextData();
    }

    // Change of name based on the name
    function chgImg(indexRow, indexCol, ScientificName) {
        if (ScientificName=="Acrobolbus" || ScientificName=="Actinidia chinensis" 
            || ScientificName=="Baileyoxylon" || ScientificName=="Goebelobryum grossitextum"
            || ScientificName=="Hydnocarpus") {
            $('#row'+indexRow+"-img"+indexCol).attr("src", "imgs/"+ScientificName+".png");
            chgUrl(indexRow, indexCol, ScientificName);
        } else {
            $('#row'+indexRow+"-img"+indexCol).attr("src", "imgs/seed_1.png");
            $('#row'+indexRow+"-a"+indexCol).attr("href", "javascript:;");
        }
    }

    // Modify the hyperlinks of the corresponding rows and columns
    function chgUrl(indexRow, indexCol, ScientificName) {
      if(ScientificName=="Acrobolbus") {
        $('#row'+indexRow+"-a"+indexCol).attr("href", "../Acrobolbus/page.html");
      } else if (ScientificName=="Actinidia chinensis") {
        $('#row'+indexRow+"-a"+indexCol).attr("href", "../Actinidia/page.html");
      } else if (ScientificName=="Baileyoxylon") {
        $('#row'+indexRow+"-a"+indexCol).attr("href", "../Baileyoxylon/page.html");
      } else if (ScientificName=="Goebelobryum grossitextum") {
        $('#row'+indexRow+"-a"+indexCol).attr("href", "../Goe/page.html");
      } else if (ScientificName=="Hydnocarpus") {
        $('#row'+indexRow+"-a"+indexCol).attr("href", "../Hyd/page.html");
      } else { // No connection is created if the condition is not met
        $('#row'+indexRow+"-a"+indexCol).attr("href", "javascript:;");
      }
    }

    // Populate the query results panel with content based on the loaded data
    function initResultDb() {
      let strHtml = ''
      $.each(lists, function(index, item){
        // With a clear destination address, add it to the href here
        if(item.ScientificName=="Acrobolbus") {
          strHtml += '<a class="search-dropdown-item" style="display:none;" href="../Acrobolbus/page.html">'+item.ScientificName+'</a>'
        } else if (item.ScientificName=="Actinidia chinensis") {
          strHtml += '<a class="search-dropdown-item" style="display:none;" href="../Actinidia/page.html">'+item.ScientificName+'</a>'
        } else if (item.ScientificName=="Baileyoxylon") {
          strHtml += '<a class="search-dropdown-item" style="display:none;" href="../Baileyoxylon/page.html">'+item.ScientificName+'</a>'
        } else if (item.ScientificName=="Goebelobryum grossitextum") {
          strHtml += '<a class="search-dropdown-item" style="display:none;" href="../Goe/page.html">'+item.ScientificName+'</a>'
        } else if (item.ScientificName=="Hydnocarpus") {
          strHtml += '<a class="search-dropdown-item" style="display:none;" href="../Hyd/page.html">'+item.ScientificName+'</a>'
        } else { // No connection is created if the condition is not met
          strHtml += '<a class="search-dropdown-item" style="display:none;" href="javascript:void(0);">'+item.ScientificName+'</a>'
        }
      })
      strHtml += '<a class="search-dropdown-item" id="noResult" style="display:none;" href="javascript:void(0);">no result</a>'
      $('.search-dropdown-container').html(strHtml)
    }
    // To ensure the security of data loading, 
    // use the following callback function method to load data sequentially
    // - End
  
    // Event Handling for Clicking the Forward Button on a Row
    // rowIndex: index value of the row, starting from 0
    function showPre(rowIndex) {
      if (rowIndex == 0) {   // Row 1
        if(index0 > 0) {   // If the current index is not the first one, turn forward
          index0--
        }
        if(index0 == 0) {   // Hide the forward button on line 1 when you reach bar 1 
          $('#btn-pre0').hide()
        }
        // Updating the names of plants displayed
        $('#row0-name0').html(plantList0[index0].ScientificName)
        $('#row0-name1').html(plantList0[index0+1].ScientificName)
        $('#row0-name2').html(plantList0[index0+2].ScientificName)
        $('#row0-name3').html(plantList0[index0+3].ScientificName)
        // change the images
        chgImg(0, 0, plantList0[index0].ScientificName)
        chgImg(0, 1, plantList0[index0+1].ScientificName)
        chgImg(0, 2, plantList0[index0+2].ScientificName)
        chgImg(0, 3, plantList0[index0+3].ScientificName)
        // Show Backward Button
        $('#btn-next0').show()
      } else if(rowIndex == 1) {   // Row 2
        if(index1 > 0) {   // If the current index is not the first one, turn forward
          index1--
        }
        if(index1 == 0) {   // Hide the forward button on line 1 when you reach bar 1 
          $('#btn-pre1').hide()
        }
        // Updating the names of plants displayed
        $('#row1-name0').html(plantList1[index1].ScientificName)
        $('#row1-name1').html(plantList1[index1+1].ScientificName)
        $('#row1-name2').html(plantList1[index1+2].ScientificName)
        $('#row1-name3').html(plantList1[index1+3].ScientificName)
        // change the images
        chgImg(1, 0, plantList1[index1].ScientificName)
        chgImg(1, 1, plantList1[index1+1].ScientificName)
        chgImg(1, 2, plantList1[index1+2].ScientificName)
        chgImg(1, 3, plantList1[index1+3].ScientificName)
        // Show Backward Button
        $('#btn-next1').show()
      }
    }
  
    // Event Handling for Clicking a Row's Backward Button
    // rowIndex: index value of the row, starting from 0
    function showNext(rowIndex) {
      if (rowIndex == 0) {   // Row 1
        if(index0+4 < plantNum0) {   // Current index +2 is not the last 1, then flip backward
          index0++
        }
        if(index0+4 == plantNum0) {   // Hide the backward button in row 1 when the right side reaches the last bar 
          $('#btn-next0').hide()
        }
        // Updating the names of plants displayed
        $('#row0-name0').html(plantList0[index0].ScientificName)
        $('#row0-name1').html(plantList0[index0+1].ScientificName)
        $('#row0-name2').html(plantList0[index0+2].ScientificName)
        $('#row0-name3').html(plantList0[index0+3].ScientificName)
        // change the images
        chgImg(0, 0, plantList0[index0].ScientificName)
        chgImg(0, 1, plantList0[index0+1].ScientificName)
        chgImg(0, 2, plantList0[index0+2].ScientificName)
        chgImg(0, 3, plantList0[index0+3].ScientificName)
        // Show Forward Button
        $('#btn-pre0').show()
      } else if(rowIndex == 1) {   // Row 2
        if(index1+4 < plantNum1) {   // Current index +2 is not the last 1, then flip backward
          index1++
        }
        if(index1+4 == plantNum1) {   // After reaching the last 1 bar on the right side, hide the backward button on the 2nd line 
          $('#btn-next1').hide()
        }
        // Updating the names of plants displayed
        $('#row1-name0').html(plantList1[index1].ScientificName)
        $('#row1-name1').html(plantList1[index1+1].ScientificName)
        $('#row1-name2').html(plantList1[index1+2].ScientificName)
        $('#row1-name3').html(plantList1[index1+3].ScientificName)
        // change the images
        chgImg(1, 0, plantList1[index1].ScientificName)
        chgImg(1, 1, plantList1[index1+1].ScientificName)
        chgImg(1, 2, plantList1[index1+2].ScientificName)
        chgImg(1, 3, plantList1[index1+3].ScientificName)
        // Show Backward Button
        $('#btn-pre1').show()
      }
    }
