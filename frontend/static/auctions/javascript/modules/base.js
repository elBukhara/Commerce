
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