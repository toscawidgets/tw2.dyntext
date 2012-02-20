function setupPollingDynText(text_widget, data_url, interval)
{
    $.getJSON(data_url, function(data) {
        var new_text = data.text;
        
        $("#"+text_widget).text(new_text);
    });

    setTimeout( function () {
            setupPollingDynText(text_widget, data_url, interval);
    }, interval );
}
