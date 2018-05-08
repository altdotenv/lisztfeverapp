import { connect } from "react-redux";
import { actionCreators as eventActions } from "redux/modules/events";
import Container from "./container";

const mapStateToProps = (state, ownProps) => {
  const { events: { feed, total_pages }, routing: { location } } = state;
  return {
    feed,
    total_pages,
    location
  }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    getFeed: page => {
      dispatch(eventActions.getFeed(page));
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Container);
