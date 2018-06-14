import { connect } from "react-redux";
import { actionCreators as userActions } from "redux/modules/user";
import Container from "./container";

const mapDispatchToProps = (dispatch, ownProps) => {
  const { match: { params: { artistId } } } = ownProps;
  return {
    redirectListenMusic: () => {
      dispatch(userActions.redirectListenMusic(artistId))
    }
  }
}

export default connect(null, mapDispatchToProps)(Container);
