// Combine Reducers cuz reducer is mono state
// redux-thunk - Actions to store whenever I want

import { createStore, combineReducers, applyMiddleware } from "redux";
import createHistory from "history/createBrowserHistory";
import thunk from "redux-thunk";
import { routerReducer, routerMiddleware } from 'react-router-redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import { i18nState } from 'redux-i18n';
import user from "redux/modules/user";
import events from "redux/modules/events";
import artists from "redux/modules/artists";

const env = process.env.NODE_ENV;

const history = createHistory();

const middlewares = [thunk, routerMiddleware(history)];

if (env === "development"){
  const { logger } = require("redux-logger");
  middlewares.push(logger);
}

const reducer = combineReducers({
  user,
  events,
  artists,
  routing: routerReducer,
  i18nState
});

let store;

if (env === "development"){
  store = initialState =>
    createStore(reducer, composeWithDevTools(applyMiddleware(...middlewares)));
} else {
  store = initialState =>
    createStore(reducer, applyMiddleware(...middlewares));
}

export { history };

export default store();
