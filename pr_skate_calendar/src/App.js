import * as React from 'react';
import Paper from '@material-ui/core/Paper';
import { ViewState, EditingState,} from '@devexpress/dx-react-scheduler';
import {
  Scheduler,
  MonthView,
  DayView,
  WeekView,
  ViewSwitcher,
  Toolbar,
  DateNavigator,
  AppointmentTooltip,
  Appointments,
  AppointmentForm,
  EditRecurrenceMenu,
  TodayButton,
  DragDropProvider,
} from '@devexpress/dx-react-scheduler-material-ui';
import './components/cell.css'
import CalendarForm from "./components/CalendarForm";
//import { appointments, added } from "./demo-data/month-appointments";
const fs = require('fs');

//TODO import Appointments in another class and render it there?
//TODO keep working on customizing the CSS/TypeScript to make calendar cells dynamic

const appointments = [
  {
    startDate: new Date(2020, 5, 4, 9, 30),
    endDate: new Date(2020, 5, 4, 4, 30),
    formComplete: false,
    truckDate: new Date(2020, 5, 4, 3, 30),
    weekOneNameOfContact: "Reuella Jacob",
    id: 1,
  },
];

export default class App extends React.PureComponent {

  constructor(props) {
    super(props);

    this.state = {
      data: appointments,
      currentDate: new Date('2020-06-2'),
      currentViewName: "Month",
    };
    console.log(props);

    this.onCommitChanges = this.commitChanges.bind(this);
    console.log(props);

    this.currentViewNameChange = currentViewName => {
      this.setState({ currentViewName });
    };
  }

  /*renderAppointmets(props) {
    return (
        <React.Fragment>
          <p>Week One Name of Contact: {{props.appointments.weekOneNameOfContact}}</p>
        </React.Fragment>
    );
  }*/

  commitChanges({ added, changed, deleted }) {
    this.setState((state) => {
      let { data } = state;
      if (added) {
        console.log("before: "); //logging the appointments before adding
        console.log(this.appointments);
        const startingAddedId = data.length > 0 ? data[data.length - 1].id + 1 : 0; //assigning ID to the new appointment
        data = [...data, { id: startingAddedId, ...added }]; //adding the appointment to the array (data)

        console.log("after: "); //console log after updating it
        console.log(this.appointments);
      }
      if (changed) { //TODO FIX SWAPPING OF START DATE AND END DATE
        data = data.map(appointment => (
            //if(changed[appointment.startDate] > changed[appointment.endDate]) {
            changed[appointment.id] ? { ...appointment, ...changed[appointment.id] } : appointment));
        console.log(data); //to see the data changes being logged in the console
        //} else {
        // console.log("start date greater than end date");
        // }

      }
      if (deleted !== undefined) {
        data = data.filter(appointment => appointment.id !== deleted);
      }
      this.appointments = data; //updating the appointments array
      return { data };
    });
  }

  saveToApts = (props) => {
    console.log('saveToApts:')
    console.log(props)
    var json = JSON.stringify(this.appointments)
    console.log(json)

    console.log('END saveToApts')
    // fs.writeFile("output.json", json, 'utf8', function (err) {
    //     if (err) {
    //         console.log("An error occured while writing JSON Object to File.");
    //         return console.log(err);
    //     }

    //     console.log("JSON file has been saved.");
    // });

  }

  render() {
    const { data, currentViewName, currentDate } = this.state;

    return (
        <Paper>
          <Scheduler
              data={data}
          >
            <ViewState
                currentViewName={currentViewName}
                onCurrentViewNameChange={this.currentViewNameChange}
                defaultCurrentDate={currentDate}
            />

            <EditingState onCommitChanges={this.onCommitChanges} />

            <MonthView/>
            <WeekView startDayHour={10} endDayHour={19} />
            <DayView />

            <Toolbar />
            <button onClick={ this.saveToApts({data}) }>Save Changes</button>
            <TodayButton />
            <DateNavigator />
            <ViewSwitcher />

            <EditRecurrenceMenu />
            <Appointments className='calendarEvent' />
            <AppointmentTooltip
                showCloseButton
                showDeleteButton
                showOpenButton
            />

            <AppointmentForm />
            <DragDropProvider
                allowDrag={({ allDay }) => !allDay}
                allowResize={() => true}/>
          </Scheduler>
        </Paper>
    );
  }
}