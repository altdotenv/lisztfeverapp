import { connect } from "react-redux";
import { actionCreators as eventActions } from "redux/modules/events";
import Container from "./container";
import { withRouter } from 'react-router-dom';

const mapStateToProps = (state, ownProps) => {
  const { events: { feed }, routing: { location } } = state;
  return {
    feed,
    location
  }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    getFeed: () => {
      dispatch(eventActions.getFeed());
    }
  }
}

// const mapStateToProps = (state, ownProps) => {
//   const { events: { feed, total_pages }, routing: { location } } = state;
//   return {
//     feed,
//     total_pages,
//     location
//   }
// }
//
// const mapDispatchToProps = (dispatch, ownProps) => {
//   return {
//     getFeed: page => {
//       dispatch(eventActions.getFeed(page));
//     }
//   }
// }

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(Container));
