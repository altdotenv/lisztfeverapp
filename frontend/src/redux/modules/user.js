// imports
import { push } from "react-router-redux";

// actions
const SAVE_TOKEN = "SAVE_TOKEN";
const LOGOUT = "LOGOUT";

// action creators
function saveToken(token){
  return {
    type: SAVE_TOKEN,
    token
  }
}
function logout() {
  return {
    type: LOGOUT
  }
}
//API actions
function facebookLogin(access_token){
  return function(dispatch){
    fetch("/user/login/facebook/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        access_token
      })
    })
    .then(response => response.json())
    .then(json => {
      if (json.token) {
        dispatch(saveToken(json.token));
      }
    })
    .catch(err => console.log(err));
  };
}

function redirectSignedRequest(signed_request, path){
  return async (dispatch, getState) => {
    const tokenBySignedRequest = await facebookSignedRequest(signed_request);
    if(tokenBySignedRequest === 401){
      console.log("Authorization error")
      dispatch(push("/error"))
    }
    dispatch(saveToken(tokenBySignedRequest.token, true))
    dispatch(push(`/${path}`))
  }
}

function facebookSignedRequest(signed_request){
  return fetch("/user/signed_request/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      signed_request
    })
  })
  .then(response => {
    if(response === 401){
      return 401;
    }
    return response.json()
  })
  .catch(err => console.log(err));
}

function usernameLogin(username, password){
  return function(dispatch){
    fetch("/rest-auth/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username,
        password
      })
    })
    .then(response => response.json())
    .then(json => {
      if (json.token) {
        dispatch(saveToken(json.token));
      }
    })
    .catch(err => console.log(err));
  }
}

function createAccount(username, password, email, name){
  return function(dispatch){
    fetch("/rest-auth/registration/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username,
        password1: password,
        password2: password,
        email,
        name
      })
    })
    .then(response => response.json())
    .then(json => {
      dispatch(saveToken(json.token));
    })
    .catch(err => console.log(err));
  }
}

// initial state

const initialState = {
  isLoggedIn: localStorage.getItem("jwt") ? true : false,
  token: localStorage.getItem("jwt")
};

// reducer

function reducer(state=initialState, action){
  switch (action.type){
    case SAVE_TOKEN:
      return applySetToken(state, action);
    case LOGOUT:
      return applyLogout(state, action);
    default:
      return state;
  }
}

// reducer functions
function applySetToken(state, action) {
  const {token} = action;
  localStorage.setItem("jwt", token);
  return {
    ...state,
    isLoggedIn: true,
    token: token
  };
}

function applyLogout(state, action) {
  localStorage.removeItem("jwt");
  return {
    ...state,
    isLoggedIn: false
  };
}

// exports
const actionCreators = {
  facebookLogin,
  usernameLogin,
  createAccount,
  logout,
  redirectSignedRequest
};

export { actionCreators }
// reducer export

export default reducer;
