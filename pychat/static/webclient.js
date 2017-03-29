"use strcit";

// polling interval (milliseconds)
var INTERVAL = 1000;

/**
 * poll chat server
 *
 * @param {boolean} scrollDown scroll down to latest message after
 *     successful request to server?
 */
function poll(scrollDown) {
  if (typeof(scrollDown) === "undefined") {
    scrollDown = false;
  }

  var div_messages = document.getElementById("messages");

  var success = function(data) {
    var html = [];
    for (var i = 0; i < data.length; i++) {
      var msg = data[i];
      html.push('<div class="message">',
                '<span class="author">', msg.nickname, '</span>',
                '<span class="time">', msg.time, '</span><br/>',
                '<span class="text">', msg.message, '</span>',
                '</div>');
    }
    div_messages.innerHTML = html.join("");
    if (scrollDown) {
      div_messages.scrollTop = div_messages.scrollHeight;
    }
  };

  $.ajax({
    dataType: "json",
    url: "/chat/get_all_messages",
    success: success
  });
}


/**
 * Post a chat message to the server
 *
 * @param {string} nickname User's nickname
 * @param {string} message Chat message
 */
function post_message(nickname, message) {
  var data = {
    'nickname': nickname,
    'message': message,
  };
  $.ajax({
    type: "POST",
    dataType: "json",
    url: "/chat/post",
    data: JSON.stringify(data),
    contentType: "application/json; charset=utf-8",
    // TODO success: function() {},
    // TODO error: function() {} 
  });
}


window.setInterval(poll, INTERVAL);


$('#inputfield').keyup(function(e){
  if(e.keyCode == 13) {  // enter key
    var message = e.target.value;
    var nickname = document.getElementById("nickname").value;
    post_message(nickname, message);
    // reset input field
    e.target.value = "";
    // poll server...
    poll(true);
  }
});
