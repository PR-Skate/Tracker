//DEFINITIONS
var Moment = require('moment');

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

function stringContainsIgnoreCase(baseString, inputString) {
    return baseString.toUpperCase().includes(inputString.toUpperCase());
}

function stringDoesNotContainsIgnoreCase(baseString, inputString) {
    return !stringContainsIgnoreCase(baseString, inputString);
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
    var dateFormats = ['MMMM D, YYYY, H:mm A', 'YYYY-MM-DD', 'MM-DD-YYYY hh:mm A']
    result = Moment(value, dateFormats, true); // python toString
    console.log(result.parsingFlags())
    if (result.isValid()) {
        return result.toDate();
    }
}

console.log(stringToDate("June 6, 2020, 12:56 a.m."));

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

function dateToday(baseDateAsString) {
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


/** Date-time */
function dateTimeIs(baseDateTimeAsString, inputDateTimeAsString){
 return dateIs(baseDateTimeAsString, inputDateTimeAsString);
}

function dateTimeIsNot(baseDateTimeAsString, inputDateTimeAsString){
    return !dateIs(baseDateTimeAsString, inputDateTimeAsString);
}

function dateTimeBefore(baseDateTimeAsString, inputDateTimeAsString){
    return dateBefore(baseDateTimeAsString, inputDateTimeAsString);
}

function dateTimeAfter(baseDateTimeAsString, inputDateTimeAsString){
    return dateAfter(baseDateTimeAsString, inputDateTimeAsString);
}

function dateTimeBetween(baseDateTimeAsString, inputDateTimeAsString){
    return dateBetween(baseDateTimeAsString, inputDateTimeAsString);
}

function dateTimeLastNDays (baseDateTimeAsString, inputDateTimeAsString){
    return dateLastNDays(baseDateTimeAsString, inputDateTimeAsString);
}


function dateTimeNextNDays(baseDateTimeAsString, inputDateTimeAsString){
    return dateNextNDays(baseDateTimeAsString, inputDateTimeAsString);
}

function dateTimeYesterday (baseDateTimeAsString){
    return dateYesterday(baseDateTimeAsString);
}

function dateTimeToday (baseDateTimeAsString){
    return dateToday(baseDateTimeAsString);
}

function dateTimeTomorrow (baseDateTimeAsString, inputDateTimeAsString){
    return dateTomorrow(baseDateTimeAsString, inputDateTimeAsString);
}

function dateTimeLast7Days (baseDateTimeAsString){
     return dateLast7Days(baseDateTimeAsString);
}

function dateTimeLast30Days (baseDateTimeAsString){
     return dateLast30Days(baseDateTimeAsString);
}

function dateTimeLast60Days (baseDateTimeAsString){
     return dateLast60Days(baseDateTimeAsString);
}

function dateTimeLast90Days (baseDateTimeAsString){
     return dateLast90Days(baseDateTimeAsString);
}

function dateTimeLast120Days (baseDateTimeAsString){
     return dateLast120Days(baseDateTimeAsString);
}

function dateTimeNext7Days (baseDateTimeAsString){
     return dateNext7Days(baseDateTimeAsString);
}

function dateTimeNext30Days (baseDateTimeAsString){
     return dateNext30Days(baseDateTimeAsString);
}

function dateTimeNext60Days (baseDateTimeAsString){
     return dateNext60Days(baseDateTimeAsString);
}

function dateTimeNext90Days (baseDateTimeAsString){
     return dateNext90Days(baseDateTimeAsString);
}

function dateTimeNext120Days (baseDateTimeAsString){
     return dateNext120Days(baseDateTimeAsString);
}

function dateTimeLastNWeeks(baseDateAsString, inputNumberAsString) {
    return dateLastWeek(baseDateAsString, inputNumberAsString);
}

function dateTimeNextNWeeks(baseDateAsString, inputNumberAsString) {
    return dateNextWeek(baseDateAsString, inputNumberAsString);
}

function dateTimeLastWeek(baseDateAsString) {
    return dateLastWeek(baseDateAsString);
}

function dateTimeThisWeek(baseDateAsString) {
    return dateThisWeek(baseDateAsString);
}

function dateTimeNextWeek(baseDateAsString) {
    return dateNextWeek(baseDateAsString);
}

function dateTimeCurrentAndPreviousWeek(baseDateAsString){
    return dateCurrentAndPreviousWeek(baseDateAsString);
}

function dateTimeCurrentAndNextWeek(baseDateAsString){
    return dateCurrentAndNextWeek(baseDateAsString);
}

function dateTimeLastNMonths(baseDateAsString, inputNumberAsString) {
    return dateLastNMonths(baseDateAsString, inputNumberAsString);
}

function dateTimeNextNMonths(baseDateAsString, inputNumberAsString) {
    return dateNextNMonths(baseDateAsString, inputNumberAsString);
}

function dateTimeThisMonth(baseDateAsString) {
    return dateThisMonth(baseDateAsString);
}

function dateTimeNextMonth(baseDateAsString) {
    return dateNextMonth(baseDateAsString)
}

function dateTimeLastMonth(baseDateAsString) {
    return dateLastMonth(baseDateAsString)
}

function dateTimeCurrentAndPreviousMonth(baseDateAsString) {
    return dateCurrentAndPreviousMonth(baseDateAsString);
}

function dateTimeCurrentAndNextMonth(baseDateAsString) {
    return dateCurrentAndPreviousMonth(baseDateAsString);
}

function dateTimeLastNYears(baseDateAsString, inputNumberAsString) {
    return dateLastNYears(baseDateAsString, inputNumberAsString);
}

function dateTimeNextNYears(baseDateAsString, inputNumberAsString) {
    return dateNextNYears(baseDateAsString, inputNumberAsString);
}

function dateTimeThisYear(baseDateAsString) {
    return dateThisYear(baseDateAsString);
}

function dateTimeNextYear(baseDateAsString) {
    return dateNextYear (baseDateAsString);
}

function dateTimeLastYear(baseDateAsString) {
    return dateLastYear(baseDateAsString);
}

function dateTimeCurrentAndPreviousYear(baseDateAsString) {
    return dateCurrentAndPreviousYear(baseDateAsString);
}

function dateTimeCurrentAndNextYear(baseDateAsString) {
    return dateCurrentAndNextYear(baseDateAsString);
}

function dateTimeOn(baseDateAsString, inputDateTimeAsString){
    let date = new Date(baseDateAsString);
    let input = new Date(inputDateTimeAsString);

    return date.getDate() === input.getDate();
}

function dateTimeAt(baseDateAsString, inputDateTimeAsString){
    let date = new Date(baseDateAsString);
    let input = new Date(inputDateTimeAsString);

    return date.getTime() === input.getTime();
}
//List      has, does not have, is empty, is not empty
function listContains(){
    if (list.forEach(checkElement(item, index, value))) return true;

    return false;
}

//todo: This may need to be fixed. Should return false if an element exists. Otherwise, the list does not contain the search value.
//How does this differ between dates, datetimes, numbers, etc ?
function listDoesNotContain(list){
    if (list.forEach(checkElement(item, index, value))) return false;

    return  true;
}


function listIsEmpty(list){
return list != null || list.length === 0
}


function listIsNotEmpty(list){
    return list != null && list.length > 0
}

function checkElement(item, index, value){
    return item === value
}

//Checkbox
function checkboxIsTrue(value){
    return value;
}

function checkboxIsFalse(value){
    return !value;
}


//EXPORTS

//OBJECTS
exports.objectIsEmpty = objectIsEmpty
exports.objectIsNotEmpty = objectIsNotEmpty

//STRINGS
exports.stringContains = stringContains
exports.stringDoesNotContains = stringDoesNotContains
exports.stringContainsIgnoreCase = stringContainsIgnoreCase
exports.stringDoesNotContainsIgnoreCase = stringDoesNotContainsIgnoreCase
exports.stringIs = stringIs
exports.stringIsNot = stringIsNot

//NUMBERS
exports.numberLessThen = numberLessThen
exports.numberGreaterThen = numberGreaterThen
exports.numberLessThenOrEqual = numberLessThenOrEqual
exports.numberGreaterThenOrEqual = numberGreaterThenOrEqual

//DATES
exports.dateIs = dateIs
exports.dateIsNot = dateIsNot
exports.dateBefore = dateBefore
exports.dateAfter = dateAfter
exports.dateBetween = dateBetween

// DAYS
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
exports.dateNext7Days = dateNext7Days
exports.dateNext30Days = dateNext30Days
exports.dateNext60Days = dateNext60Days
exports.dateNext90Days = dateNext90Days
exports.dateNext120Days = dateNext120Days

// WEEKS
exports.dateLastNWeeks = dateLastNWeeks
exports.dateNextNWeeks = dateNextNWeeks
exports.dateLastWeek = dateLastWeek
exports.dateThisWeek = dateThisWeek
exports.dateNextWeek = dateNextWeek
exports.dateCurrentAndPreviousWeek = dateCurrentAndPreviousWeek
exports.dateCurrentAndNextWeek = dateCurrentAndNextWeek

// MONTHS
exports.dateLastNMonths = dateLastNMonths
exports.dateNextNMonths = dateNextNMonths
exports.dateThisWeek = dateThisWeek
exports.dateLastWeek = dateLastWeek
exports.dateNextWeek = dateNextWeek
exports.dateCurrentAndPreviousMonth = dateCurrentAndPreviousMonth
exports.dateCurrentAndNextMonth = dateCurrentAndNextMonth

// YEARS
exports.dateLastNYears = dateLastNYears
exports.dateNextNYears = dateNextNYears
exports.dateThisYear = dateThisYear
exports.dateLastYear = dateLastYear
exports.dateNextYear = dateNextYear
exports.dateCurrentAndPreviousYear = dateCurrentAndPreviousYear
exports.dateCurrentAndNextYear = dateCurrentAndNextYear

//Date-time
exports.dateTimeIs = dateTimeIs
exports.dateTimeIsNot = dateTimeIsNot
exports.dateTimeBefore = dateTimeBefore
exports.dateTimeAfter = dateTimeAfter
exports.dateTimeBetween = dateTimeBetween
exports.dateTimeToday = dateTimeToday
exports.dateTimeYesterday = dateTimeYesterday
exports.dateTimeTomorrow = dateTimeTomorrow
exports.dateTimeLastNDays = dateTimeLastNDays
exports.dateTimeLast7Days = dateTimeLast7Days
exports.dateTimeLast30Days = dateTimeLast30Days
exports.dateTimeLast60Days = dateTimeLast60Days
exports.dateTimeLast90Days = dateTimeLast90Days
exports.dateTimeLast120Days = dateTimeLast120Days
exports.dateTimeNextNDays = dateTimeNextNDays
exports.dateTimeLastWeek = dateTimeLastWeek
exports.dateTimeThisWeek = dateTimeThisWeek
exports.dateTimeNextWeek = dateTimeNextWeek
exports.dateTimeCurrentAndPreviousWeek = dateTimeCurrentAndPreviousWeek
exports.dateTimeCurrentAndNextWeek = dateTimeCurrentAndNextWeek
exports.dateTimeCurrentAndPreviousMonth = dateTimeCurrentAndPreviousMonth
exports.dateTimeCurrentAndNextMonth = dateTimeCurrentAndNextMonth
exports.dateTimeLastNWeeks = dateTimeLastNWeeks
exports.dateTimeNextNWeeks = dateTimeNextNWeeks
exports.dateTimeLastWeek = dateTimeLastWeek
exports.dateTimeThisMonth = dateTimeThisMonth
exports.dateTimeNextMonth = dateTimeNextMonth
exports.dateTimeCurrentAndPreviousMonth = dateTimeCurrentAndPreviousMonth
exports.dateTimeCurrentAndNextMonth = dateTimeCurrentAndNextMonth
exports.dateTimeLastNYears = dateTimeLastNYears
exports.dateTimeNextNYears = dateTimeNextNYears
exports.dateTimeThisYear = dateTimeThisYear
exports.dateTimeNextYear = dateTimeNextYear
exports.dateTimeLastYear = dateTimeLastYear
exports.dateTimeCurrentAndPreviousYear = dateTimeCurrentAndPreviousYear
exports.dateTimeCurrentAndNextYear = dateTimeCurrentAndNextYear
exports.dateTimeLastNMonths = dateTimeLastNMonths
exports.dateTimeNextNMonths = dateTimeNextNMonths
exports.dateTimeOn = dateTimeOn
exports.dateTimeAt = dateTimeAt

//List
exports.listContains = listContains
exports.listDoesNotContain = listDoesNotContain
exports.listIsEmpty = listIsEmpty
exports.listIsNotEmpty = listIsNotEmpty

//Checkbox
exports.checkboxIsTrue = checkboxIsTrue
exports.checkboxIsFalse = checkboxIsFalse

exports.stringToDate = stringToDate