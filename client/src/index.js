import "./index.css";
import { Grommet }  from 'grommet'; 
import { grommet } from "grommet/themes";
import React from "react";
import ReactDOM from "react-dom";
import App from "./components/app";
import * as serviceWorker from "./serviceWorker";
import { Provider } from "react-redux";
import { createStore } from "redux";
import AppReducers from "./reducers";

const store = createStore(AppReducers);

ReactDOM.render(
  <Grommet theme={grommet}>
    <Provider store={store}>
      <App />
    </Provider>
  </Grommet>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
