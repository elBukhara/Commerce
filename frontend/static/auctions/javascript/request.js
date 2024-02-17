import { listingApi, userStatus, getCookie, makeRequest, deleteRequest } from './api.js';
import { idOfListing } from './modules/url.js';

const listingId = idOfListing();
const listing = await listingApi(listingId);
const user = await userStatus();
const csrftoken = getCookie('csrftoken');

const makeForm = document.querySelector('#request-form');
const deleteForm = document.querySelector('#delete-form');
 
const btn = document.querySelector('#request-btn');
const requestedText = document.querySelector('#requested-text');

if (user.is_authenticated) {
  if (!listing.is_added_request) {
    makeRequestForm();
  } else {
    btn.dataset.bsTarget = "#deleteRequest";
  
    requestedText.textContent = listing.requested_text[0].text;
    deleteRequestForm();
  }       
} else {
  btn.removeAttribute('data-bs-target');
  btn.removeAttribute('data-bs-toggle');
}

function makeRequestForm() {
  makeForm.addEventListener('submit', async (event) => {
      event.preventDefault(); // prevent form submission
  
      const username = user.user_profile.id;
      const listing = listingId;
      const text = document.querySelector('#request-text').value;
  
      const data = {
        user: username,
        listing: listing,
        text: text
      };
      
      await makeRequest(data, csrftoken);
  });
}

function deleteRequestForm() {
  deleteForm.addEventListener('submit', async (event) => {
    event.preventDefault(); 

    const requestId = listing.requested_text[0].id;

    await deleteRequest(requestId, csrftoken);
  }); 
}