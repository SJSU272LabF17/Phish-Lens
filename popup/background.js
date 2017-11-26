chrome.tabs.onUpdated.addListener(function(tabid, changeinfo, tab) {
    var url = tab.url;
        if (url !== undefined && changeinfo.status == "complete") {
          var parts = url.split("/");
          url = parts[0] + "//" + parts[2];
          if(url != 'chrome://newtab') {
            chrome.storage.local.set({'PhisingId': 1312312312312}, function() {
          // Notify that we saved.
          alert('save');
            chrome.storage.local.get('PhisingId', function(result){
              alert(result.PhisingId);
              });
        });
            chrome.notifications.create(url, {
                type: 'basic',
                iconUrl: 'icon.png',
                title: "Phising attact detected",
                message: url
             }, function(notificationId) {});
          }
    }
});


$( document ).ready(function() {
    alert(123);
});
