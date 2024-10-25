function getYear(year) {
	if (year) {
		return year.match(/[\d]{4}/); // This is regex (https://en.wikipedia.org/wiki/Regular_expression)
	}
}

function iterateRecords(data) {

	console.log(data);

	$.each(data.result.records, function (recordKey, recordValue) {

		var recordTitle = recordValue["dc:title"];
		var recordYear = getYear(recordValue["dcterms:temporal"]);
		var recordImage = recordValue["150_pixel_jpg"];
		var recordDescription = recordValue["dc:description"];

		if (recordTitle && recordYear && recordImage && recordDescription) {

			if (recordYear < 1900) { // Only get records from the 19th century

				$("#records").append(
					$('<article class="record">').append(
						$('<h2>').text(recordTitle),
						$('<h3>').text(recordYear),
						$('<img>').attr("src", recordImage),
						$('<p>').text(recordDescription)
					)
				);

			}

		}

	})

	setTimeout(function () {
		$("body").addClass("loaded"); // 這個的意思是讓程式運行至此後，在body元素上"loaded"這個分類，代表他現在是處於所有的資料都加載完成的狀態。
	}, 2000); //這個方程式是為了要讓網頁更加的圓滑，大部分時候網頁的資料會瞬間加載好，寫這個方程式可以讓兩個操作之間有一點延遲。也就是資料加載好之後，延遲兩秒在運行這個方程式。

	$("#filter-count strong").text($(".record:visible").length); // #filter-count strong是指定更改html中id為#filter-count中的strong元素.
	// record: visible可搜尋的文字範圍定義為能被看到的。 length則是計算共有幾個元素被返回。.text()方法則是把第一個指定更改的標籤內元素改成第二段程式碼返回的數字。

	$("#filter-text").keyup(function () {
		var searchTerm = $(this).val();
		console.log(searchTerm);
		$(".record").hide();
		$(".record:contains('" + searchTerm + "')").show();
		$("#filter-count strong").text($(".record:visible").length);
	}); //
}

$(document).ready(function () {

	var data = {
		resource_id: "9eaeeceb-e8e3-49a1-928a-4df76b059c2d",
		limit: 50
	}

	$.ajax({
		url: "https://data.qld.gov.au/api/3/action/datastore_search",
		data: data,
		dataType: "jsonp", // We use "jsonp" to ensure AJAX works correctly locally (otherwise XSS).
		cache: true,
		success: function (data) {
			iterateRecords(data);
		}
	});

});