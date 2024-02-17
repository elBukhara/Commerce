import { idOfListing } from './modules/url.js';
import { closeListing, listingApi } from './api.js';
import { comments, requests } from './modules/base.js';


let listingId = idOfListing();
const listing = await listingApi(listingId);
comments(listing.comments);
requests(listing.requests);


const radios = document.getElementsByClassName('form-check-input');
const submitBtn = document.querySelector('#submit-sell');
let option;

let user;
const selectedFromRequests = document.querySelector('#request-options');
const submitRequestedUserBtn = document.querySelector("#request-submit");
submitRequestedUserBtn.disabled = true;

function base() {
    console.log(listing);
    document.querySelector('#img').src = listing.image;
    document.querySelector('#name').textContent = listing.name;
    document.querySelector('#description').textContent = listing.description;
    document.querySelector('#category').textContent = listing.category;
    document.querySelector('#price').textContent = listing.price;
    document.querySelector('#status').textContent = (listing.is_active == true) ? "active" : "closed";
    document.querySelector('#seller').textContent = listing.seller_username;
    document.querySelector('#requests').textContent = listing.requests.length;
    document.querySelector('#requests-count').textContent = listing.requests.length;
    document.querySelector('#watchlist').textContent = listing.watchlist.length;   
    
    if (listing.is_active == false) {
        document.querySelector('#close-listing-btn').className = "d-none";
    }
    
    if (listing.requests.length > 0) {
    
        for (let i = 0; i < listing.requests.length; i++) {
            
            let request = listing.requests[i];
            let id = request.user_id;
            let name = request.user__username;
    
            const option = document.createElement('option');
            option.value = id;
            option.innerHTML = `${name}`
    
            document.querySelector('#request-options').appendChild(option);
    
        }
    
    } else {
        document.querySelector('#request-message').textContent = "No requests to your listing yet";
        document.querySelector('#request-submit').disabled = true; 
    }    
    
    for (let i = 0; i < radios.length; i++) {
        
        radios[i].addEventListener('click', () => {
            
            if (radios[i].checked) {

                if (i == 0) {
                    console.log("choose an option")
                    submitBtn.disabled = true
                } else {
                    option = i;
                    submitBtn.disabled = false
                }   
                
            }

        });
    }
}
base()


submitBtn.addEventListener('click', async () => {
    console.log("sold the reason: ", option);

    let reason;

    if (option == 1) {
        reason = "otherPlace"
    } else if (option == 2) {
        reason = "other"
    }

    const answer = await closeListing(listingId, reason, 0);
    console.log(answer);

    location.reload();

})

submitRequestedUserBtn.addEventListener('click', async () => {
    const answer = await closeListing(listingId, "e-commerce", user);
    
    console.log(answer)
    location.reload();
})

selectedFromRequests.addEventListener('change', () => {
    
    user = selectedFromRequests.value;

    if (user == "test") {
        submitRequestedUserBtn.disabled = true;
    } else {
        submitRequestedUserBtn.disabled = false;
    }
});