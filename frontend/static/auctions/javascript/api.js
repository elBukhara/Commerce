
export async function watchlistApi (listing_id) {

    const response = await fetch(
        "http://127.0.0.1:8000/api/watchlist/" + listing_id
    );
    
    const responseData = await response.json();
    const message = responseData.message;

    return message
} 

export async function requestApi (listing_id) {

    const response = await fetch(
        "http://127.0.0.1:8000/api/request/" + listing_id
    );
    
    const responseData = await response.json();
    const message = responseData.message;

    return message
}

export async function listingApi(listingId) {

    const response = await fetch(
        "/api/listings/" + listingId
    );
    
    const listing = await response.json();
    
    return listing;
}

export async function closeListing(listingId, reason, user) {
    let response;

    if (user != 0) {
        response = await fetch(
            `http://127.0.0.1:8000/api/close/${listingId}/${reason}/${user}`
        );
    } else {
        response = await fetch(
            `http://127.0.0.1:8000/api/close/${listingId}/${reason}/${user}`
        );
    }

    const answer = await response.json();
    return answer
}

export async function userStatus() {

    const response = await fetch(
        "http://127.0.0.1:8000/api/user-status"
    );
    
    const status = await response.json();
    
    return status;
}

export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
}

export async function makeRequest(data, csrftoken) {
    fetch('http://127.0.0.1:8000/api/make-request', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken 
        },
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(data => {
        console.log('Request created:', data);
        location.reload();
      })
      .catch(error => {
        console.error('Error creating request:', error);
    });
}

export function deleteRequest(requestId, csrftoken) {
    fetch(`http://127.0.0.1:8000/api/delete-request/` + requestId, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken 
      },
    })
      .then(response => {
        if (response.ok) {
          location.reload();
        } else {
          console.error('Failed to delete request');
        }
      })
      .catch(error => {
        console.error('An error occurred:', error);
      });
}