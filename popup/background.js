var BackgroundColor="RED";

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {

chrome.tabs.executeScript(null,
      {code:"document.body.style.backgroundColor='" + BackgroundColor + "'"});
     

chrome.tabs.executeScript({
    file: 'alert.js'
  }); 
});

chrome.tabs.onCreated.addListener(function(tab) {         
   
chrome.tabs.executeScript(null,
      {code:"document.body.style.backgroundColor='" + BackgroundColor + "'"});

chrome.tabs.executeScript({
    file: 'alert.js'
  }); 
});
