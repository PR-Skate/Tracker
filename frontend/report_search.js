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
exports.dateIs = dateIsNot
exports.dateBefore = dateBefore
exports.dateAfter = dateAfter
exports.dateBetween = dateBetween
exports.dateLastNDays = dateLastNDays
