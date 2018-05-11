import { connect } from "react-redux";
import { actionCreators as userActions } from "redux/modules/user";
import Container from "./container";

const mapDispatchToProps = (dispatch, ownProps) => {
  const { match: { params: { path } } } = ownProps;
  return {
    redirectSignedRequest: signed_request => {
      dispatch(userActions.redirectSignedRequest(signed_request, path))
    }
  }
}

export default connect(null, mapDispatchToProps)(Container);
