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

function getStartOfTheWeek(d) {
    d = new Date(d);
    var day = d.getDay(),
        diff = d.getDate() - day;
    return new Date(d.setDate(diff));
}

function startOfMonth(date) {
    return new Date(date.getFullYear(), date.getMonth(), 1);
}

function endOfMonth(date) {
    return new Date(date.getFullYear(), date.getMonth() + 1, 0);
}

function getDateNMonthsAgo(num) {
    return Moment().subtract(num, 'month').toDate()
}

function getDateNMonthsFuture(num) {
    return Moment().add(num, 'month').toDate()
}

function startOfYear(date) {
    return new Date(date.getFullYear(), 1, 1);
}

function endOfYear(date) {
    return new Date(date.getFullYear() + 1, 1, 0);
}

function getDateNYearsAgo(num) {
    return Moment().subtract(num, 'year').toDate()
}

function getDateNYearsFuture(num) {
    return Moment().add(num, 'year').toDate()
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

function dateNextNDays(baseDateAsString, inputNumberAsString) {
    var baseDate, inputNumber;
    inputNumber = stringToNumber(inputNumberAsString);
    baseDate = stringToDate(baseDateAsString);
    const today = new Date();
    const edgeDate = new Date(today);
    edgeDate.setDate(edgeDate + inputNumber);
    return today <= baseDate && baseDate <= edgeDate;
}

function dateYesterday(baseDateAsString) {
    const today = new Date();
    const yesterday = new Date(today);
    yesterday.setDate(today - 1);
    return dateIs(baseDateAsString, yesterday.toDateString());
}

function dateToday() {
    return dateIs(baseDateAsString, new Date().toDateString());
}

function dateTomorrow(baseDateAsString) {
    const today = new Date();
    const tomorrow = new Date(today);
    tomorrow.setDate(today + 1);
    return dateIs(baseDateAsString, tomorrow.toDateString());
}

function dateLast7Days(baseDateAsString) {
    return dateLastNDays(baseDateAsString, 7);
}

function dateLast30Days(baseDateAsString) {
    return dateLastNDays(baseDateAsString, 30);
}

function dateLast60Days(baseDateAsString) {
    return dateLastNDays(baseDateAsString, 60);
}

function dateLast90Days(baseDateAsString) {
    return dateLastNDays(baseDateAsString, 90);
}

function dateLast120Days(baseDateAsString) {
    return dateLastNDays(baseDateAsString, 120);
}

function dateNext7Days(baseDateAsString) {
    return dateNextNDays(baseDateAsString, 7);
}

function dateNext30Days(baseDateAsString) {
    return dateNextNDays(baseDateAsString, 30);
}

function dateNext60Days(baseDateAsString) {
    return dateNextNDays(baseDateAsString, 60);
}

function dateNext90Days(baseDateAsString) {
    return dateNextNDays(baseDateAsString, 90);
}

function dateNext120Days(baseDateAsString) {
    return dateNextNDays(baseDateAsString, 120);
}

function dateLastNWeeks(baseDateAsString, inputNumberAsString) {
    var inputNumber = stringToNumber(inputNumberAsString)
    const today = new Date()
    const someDayNWeeksAgo = new Date(today)
    someDayNWeeksAgo.setDate(someDayNWeeksAgo - (7 * inputNumber))
    const beginningOfNWeek = getStartOfTheWeek(someDayNWeeksAgo)
    const someDayLastWeek = new Date(today)
    someDayLastWeek.setDate(someDayLastWeek - 7)
    const beginningOfLastWeek = getStartOfTheWeek(someDayLastWeek)
    const endOfLastWeek = new Date(beginningOfLastWeek)
    endOfLastWeek.setDate(endOfLastWeek + 6)
    return dateBetween(baseDateAsString, [beginningOfNWeek.toDateString(), endOfLastWeek.toDateString()])
}

function dateNextNWeeks(baseDateAsString, inputNumberAsString) {
    var inputNumber = stringToNumber(inputNumberAsString)
    const today = new Date()
    const someDayNWeeksFuture = new Date(today)
    someDayNWeeksFuture.setDate(someDayNWeeksFuture + (7 * inputNumber))
    const endOfNWeeks = getStartOfTheWeek(someDayNWeeksFuture)
    endOfNWeeks.setDate(endOfNWeeks + 6)
    const someDayNextWeek = new Date(today)
    someDayNextWeek.setDate(someDayNextWeek + 7)
    const beginningOfNextWeek = getStartOfTheWeek(someDayNextWeek)
    return dateBetween(baseDateAsString, [beginningOfNextWeek.toDateString(), endOfNWeeks.toDateString()])
}

function dateLastWeek(baseDateAsString) {
    return dateLastNWeeks(baseDateAsString, 1)
}

function dateThisWeek(baseDateAsString) {
    var startOfThisWeek = getStartOfTheWeek(new Date())
    var endOfThisWeek = getStartOfTheWeek(new Date())
    endOfThisWeek.setDate(endOfThisWeek + 6)
    return dateBetween(baseDateAsString, [startOfThisWeek.toString, endOfThisWeek.toString])
}

function dateNextWeek(baseDateAsString) {
    return dateNextNWeeks(baseDateAsString, 1)
}

function dateCurrentAndPreviousWeek(baseDateAsString) {
    return dateThisWeek(baseDateAsString) || dateLastWeek(baseDateAsString)
}

function dateCurrentAndNextWeek(baseDateAsString) {
    return dateThisWeek(baseDateAsString) || dateNextWeek(baseDateAsString)
}

function dateLastNMonths(baseDateAsString, inputNumberAsString) {
    var inputNumber = stringToNumber(inputNumberAsString);
    var someDateNMonthsAgo = getDateNMonthsAgo(inputNumber);
    var beginningOfNMonths = startOfMonth(someDateNMonthsAgo);
    var someDateLastMonth = getDateNMonthsAgo(1);
    var endOfLastMonth = endOfMonth(someDateLastMonth);

    return dateBetween(baseDateAsString, [beginningOfNMonths.toDateString(), endOfLastMonth.toDateString()])
}

function dateNextNMonths(baseDateAsString, inputNumberAsString) {
    var inputNumber = stringToNumber(inputNumberAsString);
    var someDateNextMonth = getDateNMonthsFuture(1);
    var beginningOfNextMonth = startOfMonth(someDateNextMonth);
    var someDateNextNMonths = getDateNMonthsFuture(inputNumber);
    var endOfNextNMonths = endOfMonth(someDateNextNMonths);

    return dateBetween(baseDateAsString, [beginningOfNextMonth.toDateString(), endOfNextNMonths.toDateString()])
}

function dateThisMonth(baseDateAsString) {
    var startOfThisMonth = startOfMonth(new Date())
    var endOfThisMonth = endOfMonth(new Date())
    return dateBetween(baseDateAsString, [startOfThisMonth.toDateString(), endOfThisMonth.toDateString()])
}

function dateNextMonth(baseDateAsString) {
    return dateNextNMonths(baseDateAsString, 1)
}

function dateLastMonth(baseDateAsString) {
    return dateLastNMonths(baseDateAsString, 1)
}

function dateCurrentAndPreviousMonth(baseDateAsString) {
    return dateThisMonth(baseDateAsString) || dateLastMonth(baseDateAsString)
}

function dateCurrentAndNextMonth(baseDateAsString) {
    return dateThisMonth(baseDateAsString) || dateNextMonth(baseDateAsString)
}

function dateLastNYears(baseDateAsString, inputNumberAsString) {
    var inputNumber = stringToNumber(inputNumberAsString);
    var someDateNYearsAgo = getDateNYearsAgo(inputNumber);
    var beginningOfNYears = startOfYear(someDateNYearsAgo);
    var someDateLastYear = getDateNYearsAgo(1);
    var endOfLastYear = endOfYear(someDateLastYear);

    return dateBetween(baseDateAsString, [beginningOfNYears.toDateString(), endOfLastYear.toDateString()])
}

function dateNextNYears(baseDateAsString, inputNumberAsString) {
    var inputNumber = stringToNumber(inputNumberAsString);
    var someDateNextYear = getDateNYearsFuture(1);
    var beginningOfNextYear = startOfYear(someDateNextYear);
    var someDateNextNYears = getDateNYearsFuture(inputNumber);
    var endOfNextNYears = endOfYear(someDateNextNYears);

    return dateBetween(baseDateAsString, [beginningOfNextYear.toDateString(), endOfNextNYears.toDateString()])
}

function dateThisYear(baseDateAsString) {
    var startOfThisYear = startOfYear(new Date())
    var endOfThisYear = endOfYear(new Date())
    return dateBetween(baseDateAsString, [startOfThisYear.toDateString(), endOfThisYear.toDateString()])
}

function dateNextYear(baseDateAsString) {
    return dateNextNYears(baseDateAsString, 1)
}

function dateLastYear(baseDateAsString) {
    return dateLastNYears(baseDateAsString, 1)
}

function dateCurrentAndPreviousYear(baseDateAsString) {
    return dateThisYear(baseDateAsString) || dateLastYear(baseDateAsString)
}

function dateCurrentAndNextYear(baseDateAsString) {
    return dateThisYear(baseDateAsString) || dateNextYear(baseDateAsString)
}

//EXPORTS

//OBJECTS
exports.objectIsEmpty = objectIsEmpty
exports.objectIsNotEmpty = objectIsNotEmpty

//STRINGS
exports.stringContains = stringContains
exports.stringDoesNotContains = stringDoesNotContains
exports.stringIs = stringIs
exports.stringIsNot = stringIsNot

//NUMBERS
exports.numberLessThen = numberLessThen
exports.numberGreaterThen = numberGreaterThen
exports.numberLessThenOrEqual = numberLessThenOrEqual
exports.numberGreaterThenOrEqual = numberGreaterThenOrEqual

//DATES
exports.dateIs = dateIsNot
exports.dateBefore = dateBefore
exports.dateAfter = dateAfter
exports.dateBetween = dateBetween
exports.dateToday = dateToday
exports.dateYesterday = dateYesterday
exports.dateTomorrow = dateTomorrow
exports.dateLastNDays = dateLastNDays
exports.dateLast7Days = dateLast7Days
exports.dateLast30Days = dateLast30Days
exports.dateLast60Days = dateLast60Days
exports.dateLast90Days = dateLast90Days
exports.dateLast120Days = dateLast120Days

exports.dateNextNDays = dateNextNDays
