import React from 'react';
import { Button, Form, FormGroup, Input, Container } from 'reactstrap';


export default class CalendarForm extends React.Component {
    //TODO write functions to process the forms?
    //TODO ObjectID, InstallerID, SecondInstallerID using BSON (obejctID is a string)
    //TODO Parts of the form that are calculated (include them when saving the data but not as a part of the form
    constructor(props) {
        super(props);
        this.state = { //new Boolean or just Boolean works?
            formComplete: Boolean (false),
            weekOneNameOfContact: Boolean (false),
            weekFourNameOfContact: Boolean (false),
            startDate: new Date(2020, 5, 2, 0, 0),
        };

        this.handleClick = this.handleClick.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleChangeDate = this.handleChangeDate.bind(this);

    }
    //functions were working but I think I broke them. Will fix them soon
    handleClick = (event) => {
        console.log("button works");
        console.log(this.state);
        event.preventDefault();
    }

    handleChange = (event) => {
        const name = event.target.name;
        this.setState({ [name]: event.target.value });//sets weekOneNameOfContact to true
        console.log(this.state);
    }

    handleChangeDate(date) {
        this.setState({
            startDate: date
        })
    }


    render() {
        return (
            <Form method="get" className="themed-container">
                    <h3>Dates</h3>
                    <label>Start Date:
                        <Input type="datetime-local" name="endDate"/>
                    </label>

                    <br/>
                    <label>End Date:
                        <Input type="datetime-local" name="endDate"/>
                    </label>

                    <br/>
                    <label>Receiving Date:
                        <Input type="datetime-local" name="receivingDate" />
                    </label>

                    <br/>
                    <label>Truck Date:
                        <Input type="datetime-local" name="truckDate" />
                    </label>

                    <br/>
                    <h3>Contacts</h3>
                     <label>Week One Contact:
                         <Input type="checkbox" name="weekOneNameOfContact" value={!this.state.weekOneNameOfContact} onChange={this.handleChange}/> Yes
                     </label>

                     <br/>
                     <label>Week One Contact Name:
                         <Input type="text" name="weekOneFirstNameOfContact" placeholder="First Name"/>
                         <Input type="text" name="weekOneFirstNameOfContact" placeholder="Last Name"/>
                     </label>

                     <br/>
                     <label>Week Four Contact:
                         <Input type="checkbox" name="weekFourNameOfContact" value={!this.state.weekFourNameOfContact} onChange={this.handleChange} /> Yes
                     </label>

                     <br/>
                     <label>Week Four Contact Name:
                         <Input type="text" name="weekFourFirstNameOfContact" placeholder="First Name"/>
                         <Input type="text" name="weekFourFirstNameOfContact" placeholder="Last Name"/>
                     </label>

                     <br/>
                     <div id="wrapper">
                         <label>Form Complete</label>
                         <Input type="radio" name="formComplete" value={true} onClick={this.handleChange}/> Yes
                         <br/>
                         <Input type="radio" name="formComplete" value={false} onClick={this.handleChange}/> No
                     </div>
                     <br/>
                     <Button onClick={this.handleClick}>Submit</Button>{' '}
            </Form>
        );
    }
}
