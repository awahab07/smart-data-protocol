

var GATEWAY_MESSAGES = {
    REQUESTER_INITIALIZING: "Initializing Requester ...",
    REQUESTER_AUTH_REQUEST: "Requester authenticating ...",
    REQUESTER_AUTHENTICATED: "Requester authenticated.",

    REQUESTER_WHETHER_AUTHORIZED: "CHECK Requester Authorization",
    REQUESTER_IS_AUTHORIZED: "Requester Is Authorized To Access Resources",

    REQUESTER_RESOURCE_ACCESS: "Requester requesting Resource Access",
    REQUESTER_RESOURCE_ACCESS_DENIED: "Requester Resource Access - DENIED",
    REQUESTER_RESOURCE_ACCESS_GRANTED: "Requester Resource Access - GRANTED",

    REQUESTER_RESOURCE_CHANGE_REQUEST: "Requester requesting Resource CHANGE",
    REQUESTER_RESOURCE_CHANGE_REQUEST_DENIED: "Requester Resource Change - DENIED",
    REQUESTER_RESOURCE_CHANGE_REQUEST_GRANTED: "Requester Resource Change - GRANTED",

    OWNER_INITIALIZING: "Initializing Requester ...",
    OWNER_AUTH_REQUEST: "Owner authenticating ...",
    OWNER_AUTHENTICATED: "Owner Authenticated.",
    OWNER_FILE_UPLOAD: "Owner Uploaded File",
    OWNER_NOTIFIED: "Owner Notified"
}

var GATEWAY_MESSAGES_KEYS = {};
Object.keys(GATEWAY_MESSAGES).map(key => {GATEWAY_MESSAGES_KEYS[key] = key});

jQuery.ajaxSetup({
    contentType: 'application/json; charset=utf-8',
    dataType: 'json'
});

var messageEnRoute = null;
var pendingMessages = [];

logMessage = function(Action) {
    if(messageEnRoute) {
        pendingMessages.unshift(Action);
    } else {
        messageEnRoute = Action;

        jQuery.post('/gateway/', JSON.stringify({Action, Message: GATEWAY_MESSAGES[Action]}))
        .done(function(info){console.log("Message Sent: ", info)})
        .fail(function(error){console.log("Error Sending Message: ", error)})
        .always(function(){
            messageEnRoute = null;
            if(pendingMessages.length) {
                logMessage(pendingMessages.pop());
            }
        });
    }
}
