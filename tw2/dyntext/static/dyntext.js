function setDynamicText(text_widget, new_value) {
    $("#"+text_widget).text(new_value);
}

function setupPollingDynText(text_widget, data_url, interval) {
    $.getJSON(data_url, function(data) {
        setDynamicText(text_widget, data.text);
    });

    setTimeout( function () {
            setupPollingDynText(text_widget, data_url, interval);
    }, interval );
}
