import { listingApi, watchlistApi, userStatus } from './api.js';
import { idOfListing } from './modules/url.js';
import { comments } from './modules/base.js';

const listingId = idOfListing();
const listing = await listingApi(listingId);

base();
check();

function base() {
    document.querySelector('#img').src = listing.image;
    document.querySelector('#name').textContent = listing.name;
    document.querySelector('#description').textContent = listing.description;
    document.querySelector('#category').textContent = listing.category;
    document.querySelector('#price').textContent = listing.price;
    document.querySelector('#status').textContent = (listing.is_active == true) ? "active" : "closed";
    document.querySelector('#seller').textContent = listing.seller_username;
    document.querySelector('#watchlist').textContent = listing.watchlist;

    console.log(listing)
    comments(listing.comments);
};  

const watchlistBtn = document.querySelector('#watchlist-btn')
const requestBtn = document.querySelector('#request-btn')

async function check() {
    const response = await userStatus();
    console.log(response);

    if (response.is_authenticated) {
        buttons(listing)
        
        watchlistBtn.addEventListener('click', async () => {
            
            await watchlistApi(listingId);
            buttons(await listingApi(listingId))
        })
        // requestBtn.addEventListener('click', async () => {
            
        //     await requestApi(listingId);
        //     buttons(await listingApi(listingId))
        // })
    }
}

function buttons(listing) {
    document.querySelector('#watchlist').textContent = listing.watchlist;

    if (listing.is_added_watchlist) {
        watchlistBtn.className = 'btn btn-danger remove';
        watchlistBtn.innerHTML = 'Remove from watchlists';
    } else {
        watchlistBtn.className = 'btn btn-success add';
        watchlistBtn.innerHTML = 'Add to watchlists';
    }

    if (listing.is_added_request) {
        requestBtn.className = 'btn btn-danger remove';
        requestBtn.innerHTML = 'Delete my request';
    } else {
        requestBtn.className = 'btn btn-success add';
        requestBtn.innerHTML = 'Request';
    }

}