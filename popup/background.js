chrome.tabs.onUpdated.addListener(function(tabid, changeinfo, tab) {
    var url = tab.url;
        if (url !== undefined && changeinfo.status == "complete") {
          var parts = url.split("/");
          url = parts[0] + "//" + parts[2];
          if(url != 'chrome://newtab') {
            $('#current_url').text(url);
            chrome.storage.local.set({'url': url}, function() {
          // Notify that we saved.
        //  alert('save');
            chrome.storage.local.get('PhisingId', function(result){
            //  alert(result.url);
              });
        });
            chrome.notifications.create(url, {
                type: 'basic',
                iconUrl: 'icon1.png',
                title: "Phising attack detected",
                message: url
             }, function(notificationId) {});
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
