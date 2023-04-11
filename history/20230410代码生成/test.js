function calculateDaysBetweenDates(begin, end) {
    let beginDate = new Date(begin);
    let endDate = new Date(end);
    let days = (endDate - beginDate) / (1000 * 60 * 60 * 24);
    return days;
}