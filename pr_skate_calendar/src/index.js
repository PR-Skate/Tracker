import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import DnD from "./components/DnD";
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<DnD />, document.getElementById('root'));

/*ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
); */

