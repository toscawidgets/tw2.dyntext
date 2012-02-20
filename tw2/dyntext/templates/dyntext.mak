<%namespace name="tw" module="tw2.core.mako_util"/>
<span id="${w.attrs['id']}">${w.initial_text}</span>
<script type="text/javascript">
    setupPollingDynText("${w.selector}", ${w.j('data_url')}, ${w.j('interval')});
</script>
