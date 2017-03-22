var INTERVAL = 1000;  // 1 second

/**
 * poll chat server
 */
function poll() {
  var url = "/chat/get_all_messages";

  var success = function(data) {
    console.log(data);
  };

  $.ajax({
    dataType: "json",
    url: url,
    // data: data,
    success: success
  });
}


window.setInterval(poll, INTERVAL);
