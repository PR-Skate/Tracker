import React from 'react';

export default class CalendarForm extends React.Component {
    //TODO write functions to process the forms?
    //TODO ObjectID, InstallerID, SecondInstallerID using BSON (obejctID is a string)
    //TODO Parts of the form that are calculated (include them when saving the data but not as a part of the form)
    //TODO UI (using react-bootstrap?)
    render() {
        return (
            <form>
                <div>
                <label>Start Date:
                    <input type="datetime-local" name="startDate" required/>
                </label>

                <label>
                    <input type="datetime-local" name="receivingDate"/>
                </label>

                <br/>
                 <label>Week One Contact Name:
                     <input type="checkbox" name="weekOneNameOfContact"/>
                 </label>

                 <label>Week One Contact Name:
                     <input type="text" name="weekOneFirstNameOfContact" placeholder="First Name"/>
                     <input type="text" name="weekOneFirstNameOfContact" placeholder="Last Name"/>
                 </label>

                 <br/>
                 <label>Week Four Contact Name:
                     <input type="checkbox" name="weekFourNameOfContact"/>
                 </label>

                 <label>Week Four Contact Name:
                     <input type="text" name="weekFourFirstNameOfContact" placeholder="First Name"/>
                     <input type="text" name="weekFourFirstNameOfContact" placeholder="Last Name"/>
                 </label>

                 <label>Form Complete
                     <input type="checkbox" name="formComplete"/>
                 </label>

                 <br/>
                 <button color="primary">Submit</button>{' '}
                </div>
            </form>
        );
    }
}
