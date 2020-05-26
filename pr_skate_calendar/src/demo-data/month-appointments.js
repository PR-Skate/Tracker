import React from 'react';

export const appointments = [ //is basically a list
    //months: 0 - Jan, 1 - Feb, 2 - March...
    /**
     * Appointments Model: (field name, type)
     * startDate: SchedularDateTime
     * endDate: SchedularDateTime
     * title: string
     * allDay: boolean
     * id: number/string
     * we can include additional fields
     */
    {
        title: "Website Re-Design Plan",
        startDate: new Date(2020, 4, 23, 9, 30),
        endDate: new Date(2020, 4, 23, 11, 30),
        id: "1",
        category: "incomplete"
    },
    {
        title: "Book Flights to San Fran for Sales Trip",
        startDate: new Date(2020, 4, 23, 12, 0),
        endDate: new Date(2020, 4, 23, 13, 0),
        id: "2",
        category: "complete"
    },
    {
        title: "Final Budget Review",
        startDate: new Date(2020, 4, 24, 12, 0),
        endDate: new Date(2020, 4, 24, 13, 35),
        id: "3",
        category: "incomplete"
    },
    {
        title: "Upgrade Personal Computers",
        startDate: new Date(2020, 4, 25, 15, 15),
        endDate: new Date(2020, 4, 25, 16, 30),
        id: "4",
        category: "incomplete"
    },
    {
        title: "Customer Workshop",
        startDate: new Date(2020, 4, 26, 11, 0),
        endDate: new Date(2020, 4, 26, 12, 0),
        id: "5",
        category: "complete"
    },
    {
        title: "Prepare 2015 Marketing Plan",
        startDate: new Date(2020, 4, 26, 11, 0),
        endDate: new Date(2020, 4, 26, 13, 30),
        id: "6",
        category: "incomplete"
    },
    {
        title: "Brochure Design Review",
        startDate: new Date(2020, 4, 26, 14, 0),
        endDate: new Date(2020, 4, 26, 15, 30),
        id: "7",
        category: "incomplete"
    },
    {
        title: "Vacation",
        startDate: new Date(2020, 4, 28),
        endDate: new Date(2020, 5, 7),
        id: "8",
        category: "complete"
    }
];

