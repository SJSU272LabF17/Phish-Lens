var checkbox = $("#myonoffswitch1");

$(function() {
  chrome.storage.sync.get('phish_lens_app_status', function(result) {
    if(result['phish_lens_app_status']) {
      $('#toggle-one').bootstrapToggle();
    } else {
      $('#toggle-one').bootstrapToggle('off');
    }
  });

  $('#toggle-one').change(function() {
    if($(this).prop('checked')) {

      chrome.storage.sync.set({'phish_lens_app_status': true}, function() {
    });

    } else {
      chrome.storage.sync.set({'phish_lens_app_status': false}, function() {
          // Notify that we saved.
      //window.close();
      message('Settings saved');
    });
    }
  })

  $('.listen-click').click(function() {
    if($('#toggle-one').prop('checked')) {
      window.close();
      chrome.storage.sync.set({'phish_lens_app_status': true}, function() {
    });

    } else {
      $('.site-status-safe').css('display', 'block');
      $('.app-switched-off').css('display', 'none');
      chrome.storage.sync.set({'phish_lens_app_status': false}, function() {
      message('Settings saved');
    });
    }
  })
})
