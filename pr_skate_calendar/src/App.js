import * as React from "react";
import Paper from "@material-ui/core/Paper";
import {EditingState, ViewState} from "@devexpress/dx-react-scheduler";
import {
    Appointments,
    DateNavigator,
    DayView,
    DragDropProvider,
    MonthView,
    Scheduler,
    TodayButton,
    Toolbar,
    ViewSwitcher,
    WeekView,
} from "@devexpress/dx-react-scheduler-material-ui";

import {appointments} from "./demo-data/month-appointments";

const draggingGroupName = 'appointmentsGroup';

export default class App extends React.PureComponent {
    constructor(props) {
        super(props);

        this.state = {
            data: appointments,
            currentViewName: "month"
        };
        this.currentViewNameChange = currentViewName => {
            this.setState({ currentViewName });
        };
    }

    render() {
        const { data, currentViewName } = this.state;

        return (
            <Paper>
                <Scheduler data={data}>
                    <EditingState
                        editingAppointment={({data})}
                    />
                    <ViewState
                        defaultCurrentDate="2020-05-27"
                        currentViewName={currentViewName}
                        onCurrentViewNameChange={this.currentViewNameChange}
                    />

                    <WeekView startDayHour={10} endDayHour={19}/>

                    <MonthView/>

                    <DayView/>

                    <Toolbar/>
                    <TodayButton/>
                    <DateNavigator/>
                    <ViewSwitcher/>
                    <Appointments/>
                    <DragDropProvider
                        allowDrag={({allDay}) => !allDay}
                        allowResize={() => true}
                    />
                </Scheduler>
        </Paper>
    );
    }
}
