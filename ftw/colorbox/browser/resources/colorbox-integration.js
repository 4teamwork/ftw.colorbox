jq(function() {
    jq('a.colorboxLink').colorbox({
      'photo': true,
      'current': "{current}/{total}",
      'maxWidth': '100%',
      'maxHeight': '100%'
    });
});