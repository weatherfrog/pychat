var INTERVAL = 1000;  // 1 second

/**
 * poll chat server
 */
function poll() {
  var url = "/chat/get_all_messages";

  var success = function(data) {
    // console.log(data);
  };

  $.ajax({
    dataType: "json",
    url: url,
    // data: data,
    success: success
  });
}


// window.setInterval(poll, INTERVAL);

$('#inputfield').keyup(function(e){

  if(e.keyCode == 13) {  // enter key
    // TODO reset text field and post message
    var message = e.target.value;
    var data = {
      'from_user': "TODO",
      'message': message,
    };
    $.ajax({
      type: "POST",
      dataType: "json",
      url: "/chat/post",
      data: JSON.stringify(data),
      contentType: "application/json; charset=utf-8",
      success: function() {},
      error: function() {} 
    });
  }
});
