(function(window, $){
    window.sizeAndPositionWindow = function(x, y, width, height) {
        window.resizeTo(width, height);
        window.moveTo(x, y);
    }
})(window, jQuery);

var GATEWAY_MESSAGES = {
    REQUESTER_INITIALIZING: "Initializing Requester ...",
    REQUESTER_AUTH_REQUEST: "Requester authenticating ...",
    REQUESTER_AUTHENTICATED: "Requester authenticated.",

    REQUESTER_WHETHER_AUTHORIZED: "CHECK Requester Authorization",
    REQUESTER_IS_AUTHORIZED: "Requester us Authorized",

    REQUESTER_RESOURCE_ACCESS: "Requester requesting Resource Access",
    REQUESTER_RESOURCE_ACCESS_FAILED: "Requester Resource Access - DENIED",
    REQUESTER_RESOURCE_ACCESS_GRANTED: "Requester Resource Access - GRANTED",

    REQUESTER_RESOURCE_CHANGE_REQUEST: "Requester requesting Resource CHANGE",
    REQUESTER_RESOURCE_CHANGE_REQUEST_FAILED: "Requester Resource Change - DENIED",
    REQUESTER_RESOURCE_CHANGE_REQUEST_GRANTED: "Requester Resource Change - GRANTED",

    OWNER_AUTH_REQUEST: "Owner authenticating ...",
    OWNER_AUTHENTICATED: "Owner Authenticated.",
    OWNER_NOTIFIED: "Owner Notified"
}

jQuery.ajaxSetup({
    contentType: 'application/json; charset=utf-8',
    dataType: 'json'
});

logMessage = function(messageType) {
    jQuery.post('/gateway/', JSON.stringify({messageType, logMessage: GATEWAY_MESSAGES[messageType]}))
    .done(function(info){console.log("Message Sent: ", info)})
    .fail(function(error){console.log("Error Sending Message: ", error)})
}
