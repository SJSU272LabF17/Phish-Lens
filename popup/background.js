var BackgroundColor="";
//
// chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
// chrome.tabs.executeScript(null,
//       {code:"document.body.style.backgroundColor='" + BackgroundColor + "'"});
//
//
// chrome.tabs.executeScript({
//     file: 'alert.js'
//   });
// });
// chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
//   alert(document.window.href);
// }
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
// chrome.webNavigation.onHistoryStateUpdated.addListener(function(details) {
//     // if(details.frameId === 0) {
//     //     // Fires only when details.url === currentTab.url
//     //     chrome.tabs.get(details.tabId, function(tab) {
//     //         if(tab.url === details.url) {
//     //           alert(tab.url);
//     //         }
//     //     });
//     // }
// });
// chrome.notifications.create('teast', {
//     type: 'basic',
//     iconUrl: 'icon.png',
//     title: 'Don\'t forget!',
//     message: 'You have things to do. Wake up, dude!'
//  }, function(notificationId) {});

// chrome.tabs.onCreated.addListener(function(tab) {
//
// chrome.tabs.executeScript(null,
//       {code:"document.body.style.backgroundColor='" + BackgroundColor + "'"});
//
// chrome.tabs.executeScript({
//     file: 'alert.js'
//   });
// });
