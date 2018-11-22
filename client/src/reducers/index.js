import { combineReducers } from "redux";
import posts from "./posts";

const AppActions = combineReducers({
  posts
});

export default AppActions;
