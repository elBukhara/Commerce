export function idOfListing() {

    let url = window.location.href;
    let idRegex = /\/listing\/(\d+)/;
    let match = url.match(idRegex);
    

    if (match && match.length > 1) {
        return match[1];
    }
}