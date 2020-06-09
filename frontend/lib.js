//DEFINITIONS
var moment = require('moment');
require("moment/min/locales.min");
moment.locale('cs');
console.log(moment.locale()); // cs

var jquery = require('jquery')


function getCount(parent, getChildrensChildren) {
    var relevantChildren = 0;
    var children = parent.childNodes.length;
    for (var i = 0; i < children; i++) {
        if (parent.childNodes[i].nodeType != 3) {
            if (getChildrensChildren)
                relevantChildren += getCount(parent.childNodes[i], true);
            relevantChildren++;
        }
    }
    return relevantChildren;
}

function add(containerName, type, name) {
    var container = document.getElementById(containerName);
    var input = document.createElement("input");
    input.type = type;

    input.name = name;
    container.appendChild(document.createElement("br"));
    container.appendChild(input);
    // Append a line break
    container.appendChild(document.createElement("br"));
    return false;
}

function remove(containerName) {
    var numElementsInSelection = 3
    var container = document.getElementById(containerName);
    for (var i = 0; i < numElementsInSelection; i++) {
        container.childNodes.item(container.childElementCount - 1).remove();
    }
    return false;
}


function checkSignInStatus() {

}

function logout() {
    var temp;
    if (localStorage.getItem('auth_token_dict')) {
        console.log(localStorage.getItem('auth_token_dict'))

        temp = JSON.parse(localStorage.getItem('auth_token_dict'))
        var settings = {
            "url": "/logoutall/",
            "type": "POST",
            "timeout": 0,
            "headers": {
                "Authorization": "Token " + temp.token,
                "Content-Type": "application/json",
            }
        };
        jquery.ajax(settings).done(function () {
            localStorage.removeItem('auth_token_dict')
            console.log("deleted auth token");
        });
    }
    window.location.href = "/logout";
}

function findValueByPrefix(object, prefix) {
    for (var property in object) {
        if (object.hasOwnProperty(property) &&
            property.toString().startsWith(prefix)) {
            return object[property];
        }
    }
}


function getAuthToken() {
    var settings = {
        "url": "/login/",
        "type": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json",
        },
        "data": JSON.stringify({
            "username": document.getElementById("username").value,
            "password": document.getElementById("password").value
        }),
    };
    jquery.ajax(settings).done(function (response) {
        var temp;
        localStorage.setItem("auth_token_dict", JSON.stringify(response));
        console.log("saved auth token");
        temp = localStorage.getItem("auth_token_dict")
        console.log(temp);
    });

    return !!localStorage.getItem('auth_token_dict');

}

//EXPORT
exports.add = add;
exports.remove = remove;
exports.getCount = getCount;
exports.getAuthToken = getAuthToken
exports.findValueByPrefix = findValueByPrefix
exports.logout = logout
exports.moment = moment
exports.jquery = jquery