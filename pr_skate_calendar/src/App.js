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
//import { appointments, added } from "./demo-data/month-appointments";

export default class App extends React.PureComponent {
  static appointments = [
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
    }
  ];

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

    //this.added = {}
  }

  /*added({data}) {
    const startingAddedId = data.length > 0 ? data[data.length - 1].id + 1 : 0;
    data = [...data, { id: startingAddedId, ...added }];
    appointments = data;
    return appointments;
} */

  commitChanges({ added, changed, deleted }) {
    this.setState((state) => {
      let { data } = state;
      if (added) {
        const startingAddedId = data.length > 0 ? data[data.length - 1].id + 1 : 0;
        data = [...data, { id: startingAddedId, ...added }];
        //data = added(data);
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
            <TodayButton />
            <DateNavigator />
            <ViewSwitcher />

            <EditRecurrenceMenu />
            <Appointments />

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
