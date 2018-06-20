import { connect } from "react-redux";
import { actionCreators as eventActions } from "redux/modules/events";
import Container from "./container";

const mapStateToProps = (state, ownProps) => {
  const {
    events: { eventList },
    routing: { location }
  } = state;
  return {
    eventList,
    location
  };
};

const mapDispatchToProps = (dispatch, ownProps) => {
  const {
    match: {
      params: { artistId }
    }
  } = ownProps;
  return {
    getEventByArtistId: () => {
      dispatch(eventActions.getEventByArtistId(artistId));
    }
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Container);
