import * as React from 'react';
import Paper from '@material-ui/core/Paper';
import { ViewState, EditingState } from '@devexpress/dx-react-scheduler';
import {
  Scheduler,
  MonthView,
  DayView,
  WeekView,
  ViewSwitcher,
  Appointments,
  Toolbar,
  DateNavigator,
  AppointmentTooltip,
  AppointmentForm,
  EditRecurrenceMenu,
  TodayButton,
  DragDropProvider,
} from '@devexpress/dx-react-scheduler-material-ui';
import './components/cell.css'
//import { appointments, added } from "./demo-data/month-appointments";

export default class App extends React.PureComponent {
  appointments = []

  constructor(props) {
    super(props);

    this.state = {
      data: this.appointments,
      currentDate: new Date('2020-05-21'),
      currentViewName: "Month",
    };
    console.log(props);

    this.onCommitChanges = this.commitChanges.bind(this);
    console.log(props);

    this.currentViewNameChange = currentViewName => {
        this.setState({ currentViewName });
    };
  }

  commitChanges({ added, changed, deleted }) {
    this.setState((state) => {
      let { data } = state;
      if (added) {
        console.log("before: "); //logging the appointments before adding
        console.log(this.appointments);
        const startingAddedId = data.length > 0 ? data[data.length - 1].id + 1 : 0; //assigning ID to the new appointment
        data = [...data, { id: startingAddedId, ...added }]; //adding the appointment to the array (data)
        //this.appointments = data; //updating the appointments array
        console.log("after: "); //console log after updating it
        console.log(this.appointments);
      }
      if (changed) {
        data = data.map(appointment => (
          changed[appointment.id] ? { ...appointment, ...changed[appointment.id] } : appointment));
      }
      if (deleted !== undefined) {
        data = data.filter(appointment => appointment.id !== deleted);
      }
      return { data };
    });
  }

  //not sure if this is working rn
  saveToApts = (props) => {
    this.appointments = props;
    console.log("after Submit: "); 
    console.log(this.appointments);
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

            <MonthView />
            <WeekView startDayHour={10} endDayHour={19} />
            <DayView />

            <Toolbar />
            <button onclick={ this.saveToApts({data}) }>Save Changes</button>
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
