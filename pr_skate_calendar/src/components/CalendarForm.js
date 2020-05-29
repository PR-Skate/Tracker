import React from 'react';
import Button from 'react-bootstrap/Button';

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
            weekFourContact: Boolean (false)
        };

        this.handleclick = this.handleClick.bind(this);
        this.handleChange = this.handleChange.bind(this);
        //this.setToTrue = this.setToTrue.bind(this);
    }

    handleClick = (event) => {
        console.log("button works")
        console.log(this.state);
        event.preventDefault();
    }

    handleChange(event) {
        this.setState({ weekOneNameOfContact: event.target.value }) //sets weekOneNameOfContact to true
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
                         <input type="checkbox" name="weekOneNameOfContact" value={!this.state.weekOneNameOfContact} onClick={this.handleChange}/> Yes
                     </label>

                     <label>Week One Contact Name:
                         <input type="text" name="weekOneFirstNameOfContact" placeholder="First Name"/>
                         <input type="text" name="weekOneFirstNameOfContact" placeholder="Last Name"/>
                     </label>

                     <br/>
                     <label>Week Four Contact:
                         <input type="checkbox" name="weekFourNameOfContact" value={!this.state.weekOneNameOfContact} onClick={this.handleChange}/> Yes
                     </label>

                     <label>Week Four Contact Name:
                         <input type="text" name="weekFourFirstNameOfContact" placeholder="First Name"/>
                         <input type="text" name="weekFourFirstNameOfContact" placeholder="Last Name"/>
                     </label>

                     <label>Form Complete
                         <input type="checkbox" name="formComplete"/>
                     </label>

                     <br/>
                     <Button color="primary" onClick={this.handleClick}>Submit</Button>{' '}

                </div>
            </form>
        );
    }
}
