import React from 'react';
import {Button} from 'react-bootstrap';

export default class CalendarForm extends React.Component {
    //TODO write functions to process the forms?
    //TODO ObjectID, InstallerID, SecondInstallerID using BSON (obejctID is a string)
    //TODO Parts of the form that are calculated (include them when saving the data but not as a part of the form)
    //TODO UI (using react-bootstrap?)
    constructor(props) {
        super(props);
        this.state = { //new Boolean or just Boolean works?
            formComplete: Boolean (false),
            weekOneNameOfContact: Boolean (false),
            weekFourNameOfContact: Boolean (false)
        };

        this.handleClick = this.handleClick.bind(this);
        this.handleChange = this.handleChange.bind(this);

    }
    //functions were working but I think I broke them. Will fix them soon
    handleClick = (event) => {
        console.log("button works");
        console.log(this.state);
        event.preventDefault();
    }

    handleChange(event) {
        const name = event.target.name;
        this.setState({ [name]: event.target.value });//sets weekOneNameOfContact to true
        console.log(this.state);
        //does not change the state yet but when you click on submit it updates the state. why?
    }
    //I could either create a handleChange function for each checkbox
    //or find a way to make it read the value stored in the variable, not the variable itself

    render() {
        return (
            <form method="get">
                <div>
                    <h3>Dates</h3>
                    <label>Start Date:
                        <input type="datetime-local" name="startDate" required/>
                    </label>

                    <label>End Date:
                        <input type="datetime-local" name="endDate"/>
                    </label>

                    <label>Receiving Date:
                        <input type="datetime-local" name="receivingDate" />
                    </label>

                    <label>Truck Date:
                        <input type="datetime-local" name="truckDate" />
                    </label>

                    <br/>
                    <h3>Contacts</h3>
                     <label>Week One Contact:
                         <input type="checkbox" name="weekOneNameOfContact" value={!this.state.weekOneNameOfContact} onChange={this.handleChange}/> Yes
                     </label>

                     <label>Week One Contact Name:
                         <input type="text" name="weekOneFirstNameOfContact" placeholder="First Name"/>
                         <input type="text" name="weekOneFirstNameOfContact" placeholder="Last Name"/>
                     </label>

                     <br/>
                     <label>Week Four Contact:
                         <input type="checkbox" name="weekFourNameOfContact" value={!this.state.weekFourNameOfContact} onChange={this.handleChange} /> Yes
                     </label>

                     <label>Week Four Contact Name:
                         <input type="text" name="weekFourFirstNameOfContact" placeholder="First Name"/>
                         <input type="text" name="weekFourFirstNameOfContact" placeholder="Last Name"/>
                     </label>

                     <label>Form Complete
                         <div id="wrapper">
                         <input type="radio" name="formComplete" value={true} onClick={this.handleChange}/> Yes
                         <br/>
                         <input type="radio" name="formComplete" value={false} onClick={this.handleChange}/> No
                         </div>
                     </label>

                     <br/>
                     <Button onClick={this.handleClick}>Submit</Button>{' '}

                </div>
            </form>
        );
    }
}
