function gotoSite(siteId, siteUrl) {
    fetch(`/api/site/${siteId}/visit/`)
        .then(res => res.json())
        .then(json => console.log(json))

    window.open(siteUrl)
}