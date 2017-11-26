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
          alert(tab.url);

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
