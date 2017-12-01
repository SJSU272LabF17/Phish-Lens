chrome.tabs.onUpdated.addListener(function(tabid, changeinfo, tab) {
  var url = tab.url;
  if (url !== undefined && changeinfo.status == "complete") {
    var parts = url.split("/");
    url = parts[0] + "//" + parts[2]+'/';
    var uuid;
    check(url, function(isPhish) {
      if(isPhish) {
        chrome.notifications.create(url+guid(), {
          type: 'basic',
          iconUrl: 'lens.png',
          title: "Phising attack detected",
          message: url
        }, function(notificationId) {});
      }
    });
  }
});

chrome.tabs.query({
  active: true,
  lastFocusedWindow: true
}, function(tabs) {
  // and use that tab to fill in out title and url
  var parts = tabs[0].url.split("/");
  url = parts[0] + "//" + parts[2]+'/';
  $('#current_url').text(url);
  check(url, function(isPhish) {
    if(isPhish) {
      $('.site-status-safe').css('display', 'none');
      $('.site-status-unsafe').css('display', 'block');
      $('.loading-container').css('display', 'none');
    } else {
      $('.site-status-safe').css('display', 'block');
      $('.site-status-unsafe').css('display', 'none');
      $('.loading-container').css('display', 'none');
    }
  });
});

function check(url, call) {
  var uuid;
  if(url != 'chrome://newtab') {
    $('#current_url').html(url);
    chrome.storage.local.get('uuid', function(result){
      uuid = result.uuid;
      if(typeof(uuid) === 'undefined') {
        chrome.storage.local.set({'uuid': guid()}, function() {});
      }
      $.ajax({
        url: "http://54.202.123.8:3000/api/check?url="+url+"&id="+uuid,
        cache: false,
        success: function(response){
          if(response.message === 'phishing_detected') {
            call(true);
          } else {
            call(false);
          }
        }
      });
    });
  }
}

function guid() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
    .toString(16)
    .substring(1);
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
  s4() + '-' + s4() + s4() + s4();
}
