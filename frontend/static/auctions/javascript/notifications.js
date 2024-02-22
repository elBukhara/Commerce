import { getNotification, markNotificationAsRead, getCookie } from './api.js';
import { generateMessages } from './modules/base.js';


const notifications = await getNotification();
const notificationBadge = document.querySelector('#notification-badge');

function base() {

    const unreadMessages = notifications.unread_messages;
    const allMessages = notifications.notifications;
    const countMessages = allMessages.length;

    generateMessages(allMessages, countMessages);

    if (unreadMessages > 0) {
        notificationBadge.style.display = 'inline-block';
        //notificationDropdown.style.display = 'block';
        notificationBadge.textContent = unreadMessages;
        linkUnreadMessages();
    }

    
}

if (notifications.status == 'none') {
    console.log(false)
} else {
    base()
}

function linkUnreadMessages() {
    const btn = document.querySelectorAll('.unread')
    btn.forEach( (item) =>  {
        
        item.addEventListener('click', async () => {
            const csrftoken = getCookie('csrftoken');
            const id = item.dataset.id
            // console.log(id)
            const response = await markNotificationAsRead(id, csrftoken);
            // console.log(response)
        })
    
    })
}

