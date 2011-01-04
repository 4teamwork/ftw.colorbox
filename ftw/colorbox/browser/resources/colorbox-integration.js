jq(function() {
    jq('a.colorboxLink').colorbox({
        'photo': true,
        'current': "{current}/{total}"
    });
});