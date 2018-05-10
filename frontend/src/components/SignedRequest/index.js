import { connect } from "react-redux";
import { actionCreators as userActions } from "redux/modules/user";
import { actionCreators as eventActions } from "redux/modules/events";
import Container from "./container";

const mapStateToProps = (state, ownProps) => {
  const { user: { isLoggedIn } } = state;
  return {
    isLoggedIn
  }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  const { match: { params: { eventId } } } = ownProps;
  return {
    eventSignedRequest: signed_request => {
      dispatch(userActions.eventSignedRequest(signed_request, eventId))
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Container);
