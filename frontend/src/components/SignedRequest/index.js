import { connect } from "react-redux";
import { actionCreators as userActions } from "redux/modules/user";
import Container from "./container";

const mapDispatchToProps = (dispatch, ownProps) => {
  const {
    match: {
      params: { path }
    }
  } = ownProps;
  const {
    match: {
      params: { artistId }
    }
  } = ownProps;
  if (artistId) {
    return {
      redirectSignedRequest: signed_request => {
        dispatch(userActions.redirectSignedRequest(signed_request, artistId));
      }
    };
  } else {
    return {
      redirectSignedRequest: signed_request => {
        dispatch(userActions.redirectSignedRequest(signed_request, path));
      }
    };    
  }
};

export default connect(null, mapDispatchToProps)(Container);
