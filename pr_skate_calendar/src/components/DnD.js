import React from 'react';
import { appointments } from '../demo-data/month-appointments';
import './DnD.css';


export default class DnD extends React.Component {
    state = {
        appointments: {appointments}
    }

    onDragStart = (e, id) => {
        console.log('dragstart:', id);
        e.dataTransfer.setData("id",id);
    }

    onDragOver = (e) => {
        e.preventDefault();
    }

    onDrop = (e, category) => { //change category to date eventually
        let id = e.dataTransfer.getData("id");

        let appointment = appointments.filter((apt) => {
            if(apt.WO === id) {
                //apt.startDate = date; use when I figure out how to get the date
                apt.category = category;
            }
            return apt;
        });

        this.setState({
            ...this.state,
            appointment
        });
    }

    render() {
        var appointment =  {
            incomplete: [],
            complete: []
        }
        appointments.map((apt) => {
            appointment[apt.category].push(
                <div key={apt.WO}
                    onDragStart = {(e) => this.onDragStart(e, apt.WO)}
                    draggable
                    className="draggable">
                    {apt.title}
                </div>
            );
        });

        return (
            <div>
                <div className="incomplete"
                    onDragOver={(e)=> this.onDragOver(e)}
                    onDrop={(e)=>this.onDrop(e, "incomplete")}>
                    <span>Incomplete</span>
                        {appointment.incomplete}
                 </div>
                <div className="droppable"
                    onDragOver={(e)=>this.onDragOver(e)}
                    //current needs to be dynamically changed to the date on which it is being dropped
                    onDrop={(e)=>this.onDrop(e, "complete")}>
                    <span><h2>DnD Demo</h2></span>
                    {appointment.complete}
                </div>
        </div>
        );
    }
}