
export function comments(comments) {

    if (comments.length > 0 ) {

        for (let i = 0; i < comments.length; i++) {

            const item = comments[i]

            const user = item.user__username;
            const text = item.text;

            const element = document.createElement('p');
            element.innerHTML = `
            ${user}: ${text}
            `
            document.querySelector('#comments').appendChild(element);
        }
    } else {
        
        const element = document.createElement('p');
        element.innerHTML = `No comments yet.`
        document.querySelector('#comments').appendChild(element);
    }
    
}

export function requests(requests) {

    if (requests.length > 0 ) {

        for (let i = 0; i < requests.length; i++) {

            const item = requests[i]
            const user = item.user__username;
            const text = item.text;

            const element = document.createElement('p');
            element.innerHTML = `
            <strong>${user}</strong>: ${text}
            `
            document.querySelector('#requests-text').appendChild(element);
        }
    } else {
        
        const element = document.createElement('p');
        element.innerHTML = `No requests yet.`
        document.querySelector('#requests-text').appendChild(element);
    }
    
}

export function generateMessages(allMessages, countMessages) {
    const notificationDropdown = document.querySelector('#notification-dropdown');
    
    if (countMessages > 0) {
        for (let i = 0; i < countMessages; i++) {
            const notification = allMessages[i];
            const text = notification.message;
            const listingId = notification.reference_number;
            const notificationId = notification.id;
    
            const element = document.createElement('div');

            if (notification.is_read) {    
                element.innerHTML = `
                <a class="dropdown-item" data-id="${notificationId}" href="http://127.0.0.1:8000/listing/${listingId}">${text}</a>
                <hr class="dropdown-divider">
                `    
                notificationDropdown.appendChild(element);
            } else {
                element.innerHTML = `
                <a class="dropdown-item unread" data-id="${notificationId}" href="http://127.0.0.1:8000/listing/${listingId}">${text}</a>
                <hr class="dropdown-divider">
                `    
                notificationDropdown.appendChild(element);
            } 
            // href="http://127.0.0.1:8000/listing/${listingId}"
        }

    } else {
        const element = document.createElement('div');
        element.innerHTML = `
        <li class="dropdown-item">No messages yet.</li>
        <hr class="dropdown-divider">
        `    
        notificationDropdown.appendChild(element);

    }
}