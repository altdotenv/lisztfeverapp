// imports
import { actionCreators as userActions } from "redux/modules/user";

// actions

const SET_ARTIST_LIST = "SET_ARTIST_LIST";

// action creators

function setArtistList(artistList){
  return {
    type: SET_ARTIST_LIST,
    artistList
  }
}

// api actions

function searchByTerm(searchTerm) {
  return async (dispatch, getState) => {
    const { user: { token } } = getState();
    const artistList = await searchArtists(token, searchTerm);
    if(artistList === 401){
      dispatch(userActions.logout());
    }
    dispatch(setArtistList(artistList));
  };
}

function searchArtists(token, searchTerm) {
  return fetch(`/artist/search/?terms=${searchTerm}`, {
    headers: {
      Authorization: `JWT ${token}`,
      "Content-Type": "application/json"
    }
  })
    .then(response => {
      if (response.status === 401) {
        return 401;
      }
      return response.json();
    })
    .then(json => json);
}

// initial state
const initialState = {};

// reducer
function reducer(state = initialState, action){
  switch(action.type){
    case SET_ARTIST_LIST:
      return applySetArtistList(state, action);
    default:
      return state;
  }
}
// reducer functions
function applySetArtistList(state, action){
  const { artistList } = action;
  return {
    ...state,
    artistList
  }
};

// exports
const actionCreators = {
  searchByTerm
};

export { actionCreators };

// default reducer exports
export default reducer;
