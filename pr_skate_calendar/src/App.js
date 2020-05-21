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
import { appointments } from "./demo-data/month-appointments";

export default class App extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      data: appointments,
      currentDate: new Date('2020-05-21'),
      currentViewName: "Month",
    };

    this.onCommitChanges = this.commitChanges.bind(this);

    this.currentViewNameChange = currentViewName => {
        this.setState({ currentViewName });
    };
  }

  commitChanges({ added, changed, deleted }) {
    this.setState((state) => {
      let { data } = state;
      if (added) {
        const startingAddedId = data.length > 0 ? data[data.length - 1].id + 1 : 0;
        data = [...data, { id: startingAddedId, ...added }];
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
