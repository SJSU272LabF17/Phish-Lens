chrome.tabs.onUpdated.addListener(function(tabid, changeinfo, tab) {
  var url = tab.url;
  if (url !== undefined && changeinfo.status == "complete") {
    var parts = url.split("/");
    url = parts[0] + "//" + parts[2]+'/';
    var uuid;
    chrome.storage.sync.get('phish_lens_app_status', function(result) {
      if(result['phish_lens_app_status']) {
        check(url, function(isPhish) {
          if(isPhish) {
            updatePhisingHitCount(function() {
              chrome.notifications.create(url+guid(), {
                type: 'basic',
                iconUrl: 'lens.png',
                title: "Phishing attack detected",
                message: url
              }, function(notificationId) {});
            })

          }
        });
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
  chrome.storage.sync.get('phish_lens_app_status', function(result) {
    if(result['phish_lens_app_status']) {
      check(url, function(isPhish) {
        if(isPhish) {
          updatePhisingHitCount(function() {
            $('.site-status-safe').css('display', 'none');
            $('.site-status-unsafe').css('display', 'block');
            $('.loading-container').css('display', 'none');
            $('.app-switched-off').css('display', 'none');
          });
        } else {
          $('.site-status-safe').css('display', 'block');
          $('.site-status-unsafe').css('display', 'none');
          $('.loading-container').css('display', 'none');
          $('.app-switched-off').css('display', 'none');
        }
      });
    } else {
      $('.loading-container').css('display', 'none');
      $('.site-status-unsafe').css('display', 'none');
      $('.site-status-safe').css('display', 'none');
      $('.app-switched-off').css('display', 'block');
    }
  });
});

function check(url, call) {
  var uuid;
  if(url != 'chrome://newtab' && url != 'chrome://extensions/') {
    $('#current_url').html(url);
    chrome.storage.local.get('uuid', function(result){
      uuid = result.uuid;
      if(typeof(uuid) === 'undefined') {
        chrome.storage.local.set({'uuid': guid()}, function() {});
      }
      updateTotalHitCount(function() {
        $.ajax({
          url: "http://54.202.123.8/api/check?url="+url+"&id="+uuid,
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
    });
  }
}

function updateTotalHitCount(callback) {
  chrome.storage.sync.get('total_hit_count', function(result) {
    if(typeof(result.total_hit_count) !== 'undefined') {
      var total_hit_count = result.total_hit_count;
      total_hit_count+=1;
      chrome.storage.sync.set({'total_hit_count': total_hit_count}, function() {});
    } else {
      chrome.storage.sync.set({'total_hit_count': 0}, function() {});
      chrome.storage.sync.set({'total_phishing_hit_count': 0}, function() {});
    }
    callback();
  });
}

function updatePhisingHitCount(callback) {
  chrome.storage.sync.get('total_phishing_hit_count', function(result) {
    if(typeof(result.total_phishing_hit_count) !== 'undefined') {
      var total_phishing_hit_count = result.total_phishing_hit_count;
      total_phishing_hit_count+=1;
      chrome.storage.sync.set({'total_phishing_hit_count': total_phishing_hit_count}, function() {});
    } else {
      chrome.storage.sync.set({'total_phishing_hit_count': 0}, function() {});
    }
    callback();
  });
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
