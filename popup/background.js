chrome.tabs.onUpdated.addListener(function(tabid, changeinfo, tab) {
  var url = tab.url;
  if (url !== undefined && changeinfo.status == "complete") {
    var parts = url.split("/");
    var uuid;
    url = parts[0] + "//" + parts[2]+'/';
    if(url != 'chrome://newtab') {
      $('#current_url').text(url);
      chrome.storage.local.get('uuid', function(result){
        uuid = result.uuid;
        if(typeof(uuid) === 'undefined') {
          chrome.storage.local.set({'uuid': guid()}, function() {});
        }
        $.ajax({
          url: "http://localhost:3000/api/check?url="+url+"&id="+uuid,
          cache: false,
          success: function(response){
            if(response.message === 'phishing_detected') {
              chrome.notifications.create(url+guid(), {
                type: 'basic',
                iconUrl: 'icon1.png',
                title: "Phising attack detected",
                message: url
              }, function(notificationId) {});
            }
          }
        });
      });
    }
  }
});

chrome.tabs.query({
  active: true,
  lastFocusedWindow: true
}, function(tabs) {
  // and use that tab to fill in out title and url
  var parts = tabs[0].url.split("/");
  $('#current_url').text(parts[2]);
});

function guid() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
    .toString(16)
    .substring(1);
  }
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
  s4() + '-' + s4() + s4() + s4();
}
