//DEFINITIONS
var Moment = require('moment');
require("moment/min/locales.min");
Moment.locale('cs');
console.log(Moment.locale()); // cs

var Jquery = require('jquery')

var Cookies = require('js-cookie')


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
    var temp;
    try {
        console.log(localStorage.getItem('auth_token_dict'));
        temp = JSON.parse(localStorage.getItem('auth_token_dict'));
        console.log(temp.expiry)
        if (new Date(temp.expiry) < new Date()) {
            logout()
        }
    } catch (e) {
        localStorage.removeItem('auth_token_dict')
        logout()
    }
}


function logout() {
    var temp;
    if (localStorage.getItem('auth_token_dict')) {
        console.log(localStorage.getItem('auth_token_dict'));
        temp = JSON.parse(localStorage.getItem('auth_token_dict'));
        console.log(temp.expiry)
        if (new Date(temp.expiry) > new Date()) {
            var settings = {
                "url": "/logoutall/",
                "type": "POST",
                "timeout": 0,
                "headers": {
                    "Authorization": "Token " + temp.token,
                    "Content-Type": "application/json",
                }
            };
            Jquery.ajax(settings).done(function () {
                console.log("deleted auth token");
            });
        }
        localStorage.removeItem('auth_token_dict')
    }
    console.log(window.location.href)
    if (!window.location.href.includes("/sign-in")) {
        window.location.href = "/logout";
    }
}

function findValueByPrefix(object, prefix) {
    for (var property in object) {
        if (object.hasOwnProperty(property) &&
            property.toString().startsWith(prefix)) {
            return object[property];
        }
    }
}


function login(event, token) {
    event.preventDefault()
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    getAuthToken(username, password, token);
    token = Cookies.get('csrftoken')

    var settings = {
        "url": window.location.href,
        "method": "POST",
        "async": false,
        "timeout": 0,
        "headers": {
            "Content-Length": " 133",
            "Cache-Control": " max-age=0",
            "Upgrade-Insecure-Requests": " 1",
            "Content-Type": " application/x-www-form-urlencoded",
            "Accept-Language": " en-US,en;q=0.9",
        },
        "data": "csrfmiddlewaretoken=" + token + "&username=" + username + "&password=" + password,
    };
    Jquery.ajax(settings).done(function (response) {
        window.location.href = window.location.href.includes("next=") ? window.location.href.split("next=")[1] : '/'
    });
}

function getAuthToken(username, password, token) {
    var settings = {
        "url": "/login/",
        "type": "POST",
        "timeout": 0,
        "async": false,
        "headers": {
            "X-CSRFToken": token,
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "username": username,
            "password": password
        }),
    };
    Jquery.ajax(settings).done(function (response) {
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
exports.login = login
exports.findValueByPrefix = findValueByPrefix
exports.logout = logout
exports.checkSignInStatus = checkSignInStatus
exports.moment = Moment
exports.jquery = Jquery


//DEFINITIONS
var Moment = require('moment');
require("moment/min/locales.min");
Moment.locale('cs');

var Jquery = require('jquery')

var Cookies = require('js-cookie')


//GENERAL OBJECTS

function objectIsEmpty(arg) {
    return (
        arg == null || // Check for null or undefined
        arg.length === 0 || // Check for empty String (Bonus check for empty Array)
        (typeof arg === 'object' && Object.keys(arg).length === 0) // Check for empty Object or Array
    );
}

function objectIsNotEmpty(arg) {
    return !objectIsEmpty(arg);
}


//STRINGS

function stringContains(baseString, inputString) {
    return baseString.includes(inputString);
}

function stringDoesNotContains(baseString, inputString) {
    return !stringContains(baseString, inputString);
}

function stringIs(baseString, inputString) {
    return baseString === inputString;
}

function stringIsNot(baseString, inputString) {
    return !stringIs(baseString, inputString);
}


// NUMBERS
function stringToNumber(value) {
    return parseFloat(value);
}

function numberLessThen(baseNumberAsString, inputNumberAsString) {
    var baseNumber, inputNumber;
    baseNumber = stringToNumber(baseNumberAsString);
    inputNumber = stringToNumber(inputNumberAsString);
    return baseNumber < inputNumber;
}

function numberGreaterThen(baseNumberAsString, inputNumberAsString) {
    var baseNumber, inputNumber;
    baseNumber = stringToNumber(baseNumberAsString);
    inputNumber = stringToNumber(inputNumberAsString);
    return baseNumber > inputNumber;
}

function numberLessThenOrEqual(baseNumberAsString, inputNumberAsString) {
    var baseNumber, inputNumber;
    baseNumber = stringToNumber(baseNumberAsString);
    inputNumber = stringToNumber(inputNumberAsString);
    return baseNumber <= inputNumber;
}

function numberGreaterThenOrEqual(baseNumberAsString, inputNumberAsString) {
    var baseNumber, inputNumber;
    baseNumber = stringToNumber(baseNumberAsString);
    inputNumber = stringToNumber(inputNumberAsString);
    return baseNumber >= inputNumber;
}

// DATES

function stringToDate(value) {
    var result;
    result = Moment(value, 'MMMM D, YYYY, H:mm'); // python toString
    if (result) {
        return result.toDate();
    }

    result = Moment(value, 'YYYY-MM-DD'); //HTML input type date
    if (result) {
        return result.toDate();
    }
}

function dateIs(baseDateAsString, inputDateAsString) {
    var baseDate, inputDate;
    baseDate = stringToDate(baseDateAsString);
    inputDate = stringToDate(inputDateAsString);

    return baseDate.getTime() === inputDate.getTime();
}

function dateIsNot(baseDateAsString, inputDateAsString) {
    return !dateIs(baseDateAsString, inputDateAsString);
}

function dateBefore(baseDateAsString, inputDateAsString) {
    var baseDate, inputDate;
    baseDate = stringToDate(baseDateAsString);
    inputDate = stringToDate(inputDateAsString);

    return baseDate < inputDate;
}

function dateAfter(baseDateAsString, inputDateAsString) {
    var baseDate, inputDate;
    baseDate = stringToDate(baseDateAsString);
    inputDate = stringToDate(inputDateAsString);

    return baseDate > inputDate;
}

function dateBetween(baseDateAsString, inputDatesAsStringsInList) {
    var baseDate, inputDate, inputDate2;
    baseDate = stringToDate(baseDateAsString);
    inputDate = stringToDate(inputDatesAsStringsInList[0]);
    inputDate2 = stringToDate(inputDatesAsStringsInList[1]);
    if (inputDate < inputDate2) {
        return inputDate <= baseDate && baseDate <= inputDate2;
    } else {
        return inputDate2 <= baseDate && baseDate <= inputDate;
    }
}

function dateLastNDays(baseDateAsString, inputNumberAsString) {
    var baseDate, inputNumber;
    inputNumber = stringToNumber(inputNumberAsString);
    baseDate = stringToDate(baseDateAsString);
    const today = new Date();
    const edgeDate = new Date(today);
    edgeDate.setDate(edgeDate - inputNumber);
    return edgeDate <= baseDate && baseDate <= today;
}

function dateYesterday(baseDateAsString) {
    var baseDate, inputNumber;
    inputNumber = stringToNumber(inputNumberAsString);
    baseDate = stringToDate(baseDateAsString);
    const today = new Date();
    const edgeDate = new Date(today);
    edgeDate.setDate(edgeDate - inputNumber);
    return edgeDate <= baseDate && baseDate <= today;
}

//EXPORT
exports.stringContains = stringContains
exports.stringDoesNotContains = stringDoesNotContains
exports.objectIsEmpty = objectIsEmpty
exports.objectIsNotEmpty = objectIsNotEmpty
exports.stringIs = stringIs
exports.stringIsNot = stringIsNot

exports.numberLessThen = numberLessThen
exports.numberGreaterThen = numberGreaterThen
exports.numberLessThenOrEqual = numberLessThenOrEqual
exports.numberGreaterThenOrEqual = numberGreaterThenOrEqual

exports.dateIs = dateIs
exports.dateIsNot = dateIsNot
exports.dateBefore = dateBefore
exports.dateAfter = dateAfter
exports.dateBetween = dateBetween
exports.dateLastNDays = dateLastNDays


//DEFINITIONS
var Moment = require('moment');
require("moment/min/locales.min");
Moment.locale('cs');

var Jquery = require('jquery')

var Cookies = require('js-cookie')


//GENERAL OBJECTS

function objectIsEmpty(arg) {
    return (
        arg == null || // Check for null or undefined
        arg.length === 0 || // Check for empty String (Bonus check for empty Array)
        (typeof arg === 'object' && Object.keys(arg).length === 0) // Check for empty Object or Array
    );
}

function objectIsNotEmpty(arg) {
    return !objectIsEmpty(arg);
}


//STRINGS

function stringContains(baseString, inputString) {
    return baseString.includes(inputString);
}

function stringDoesNotContains(baseString, inputString) {
    return !stringContains(baseString, inputString);
}

function stringIs(baseString, inputString) {
    return baseString === inputString;
}

function stringIsNot(baseString, inputString) {
    return !stringIs(baseString, inputString);
}


// NUMBERS
function stringToNumber(value) {
    return parseFloat(value);
}

function numberLessThen(baseNumberAsString, inputNumberAsString) {
    var baseNumber, inputNumber;
    baseNumber = stringToNumber(baseNumberAsString);
    inputNumber = stringToNumber(inputNumberAsString);
    return baseNumber < inputNumber;
}

function numberGreaterThen(baseNumberAsString, inputNumberAsString) {
    var baseNumber, inputNumber;
    baseNumber = stringToNumber(baseNumberAsString);
    inputNumber = stringToNumber(inputNumberAsString);
    return baseNumber > inputNumber;
}

function numberLessThenOrEqual(baseNumberAsString, inputNumberAsString) {
    var baseNumber, inputNumber;
    baseNumber = stringToNumber(baseNumberAsString);
    inputNumber = stringToNumber(inputNumberAsString);
    return baseNumber <= inputNumber;
}

function numberGreaterThenOrEqual(baseNumberAsString, inputNumberAsString) {
    var baseNumber, inputNumber;
    baseNumber = stringToNumber(baseNumberAsString);
    inputNumber = stringToNumber(inputNumberAsString);
    return baseNumber >= inputNumber;
}

// DATES

function stringToDate(value) {
    var result;
    result = Moment(value, 'MMMM D, YYYY, H:mm'); // python toString
    if (result) {
        return result.toDate();
    }

    result = Moment(value, 'YYYY-MM-DD'); //HTML input type date
    if (result) {
        return result.toDate();
    }
}

function dateIs(baseDateAsString, inputDateAsString) {
    var baseDate, inputDate;
    baseDate = stringToDate(baseDateAsString);
    inputDate = stringToDate(inputDateAsString);

    return baseDate.getTime() === inputDate.getTime();
}

function dateIsNot(baseDateAsString, inputDateAsString) {
    return !dateIs(baseDateAsString, inputDateAsString);
}

function dateBefore(baseDateAsString, inputDateAsString) {
    var baseDate, inputDate;
    baseDate = stringToDate(baseDateAsString);
    inputDate = stringToDate(inputDateAsString);

    return baseDate < inputDate;
}

function dateAfter(baseDateAsString, inputDateAsString) {
    var baseDate, inputDate;
    baseDate = stringToDate(baseDateAsString);
    inputDate = stringToDate(inputDateAsString);

    return baseDate > inputDate;
}

function dateBetween(baseDateAsString, inputDatesAsStringsInList) {
    var baseDate, inputDate, inputDate2;
    baseDate = stringToDate(baseDateAsString);
    inputDate = stringToDate(inputDatesAsStringsInList[0]);
    inputDate2 = stringToDate(inputDatesAsStringsInList[1]);
    if (inputDate < inputDate2) {
        return inputDate <= baseDate && baseDate <= inputDate2;
    } else {
        return inputDate2 <= baseDate && baseDate <= inputDate;
    }
}

function dateLastNDays(baseDateAsString, inputNumberAsString) {
    var baseDate, inputNumber;
    inputNumber = stringToNumber(inputNumberAsString);
    baseDate = stringToDate(baseDateAsString);
    const today = new Date();
    const edgeDate = new Date(today);
    edgeDate.setDate(edgeDate - inputNumber);
    return edgeDate <= baseDate && baseDate <= today;
}

function dateYesterday(baseDateAsString) {
    var baseDate, inputNumber;
    inputNumber = stringToNumber(inputNumberAsString);
    baseDate = stringToDate(baseDateAsString);
    const today = new Date();
    const edgeDate = new Date(today);
    edgeDate.setDate(edgeDate - inputNumber);
    return edgeDate <= baseDate && baseDate <= today;
}

//EXPORT
exports.stringContains = stringContains
exports.stringDoesNotContains = stringDoesNotContains
exports.objectIsEmpty = objectIsEmpty
exports.objectIsNotEmpty = objectIsNotEmpty
exports.stringIs = stringIs
exports.stringIsNot = stringIsNot
exports.numberLessThen = numberLessThen
exports.numberGreaterThen = numberGreaterThen
exports.numberLessThenOrEqual = numberLessThenOrEqual
exports.numberGreaterThenOrEqual = numberGreaterThenOrEqual
exports.dateIs = dateIs
exports.dateIsNot = dateIsNot
exports.dateBefore = dateBefore
exports.dateAfter = dateAfter
exports.dateBetween = dateBetween
exports.dateLastNDays = dateLastNDays
