import 'devextreme/dist/css/dx.common.css';
import 'devextreme/dist/css/dx.light.css';
import * as React from "react";
import Paper from "@material-ui/core/Paper";
import { ViewState } from "@devexpress/dx-react-scheduler";
import {
    Scheduler,
    WeekView,
    Appointments,
    Toolbar,
    DateNavigator,
    ViewSwitcher,
    MonthView,
    DayView,
    TodayButton, //FIXME Make today button go to day view instead of month view
} from "@devexpress/dx-react-scheduler-material-ui";

import {AppointmentDragging} from "devextreme-react/scheduler";

import { appointments } from "./demo-data/month-appointments";

const draggingGroupName = 'appointmentsGroup';

export default class App extends React.PureComponent {
    constructor(props) {
        super(props);

        this.state = {
            data: appointments,
            currentViewName: "work-week"
        };
        this.currentViewNameChange = currentViewName => {
            this.setState({ currentViewName });
        };
        this.onAppointmentRemove = this.onAppointmentRemove.bind(this);
        this.onAppointmentAdd = this.onAppointmentAdd.bind(this);
    }

    render() {
        const { data, currentViewName } = this.state;

        return (
            <Paper>
            <Scheduler
            id="scheduler"
        data={data}
        startDayHour={9}
        editing={true}>
            <ViewState
        defaultCurrentDate="2020-05-27"
        currentViewName={currentViewName}
        onCurrentViewNameChange={this.currentViewNameChange}
        />
        <AppointmentDragging
        group={draggingGroupName}
        onRemove={this.onAppointmentRemove}
        onAdd={this.onAppointmentAdd}
        />

        <WeekView startDayHour={10} endDayHour={19} />

        <MonthView />

        <DayView />

        <Toolbar />
            <TodayButton />
            <DateNavigator />
        <ViewSwitcher />
        <Appointments />
        </Scheduler>
        </Paper>
    );
    }

    onAppointmentRemove(e) {
        const index = this.state.appointments.indexOf(e.itemData);

        if (index >= 0) {
            this.state.appointments.splice(index, 1);

            this.setState({
                appointments: [...this.state.appointments]
            });
        }
    }

    onAppointmentAdd(e) {
        const index = this.state.tasks.indexOf(e.fromData);

        if (index >= 0) {
            this.state.appointments.push(e.itemData);

            this.setState({
                appointments: [...this.state.appointments]
            });
        }
    }
}
