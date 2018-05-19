import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as eventActions } from "redux/modules/events";

const mapDispatchToProps = (dispatch, ownProps) => {
  const { plan } = ownProps;
  return {
    handleClick: () => {
      if (plan.event.is_planned) {
        dispatch(eventActions.unplanList(plan.event.eventid));
      } else {
        dispatch(eventActions.planList(plan.event.eventid));
      }
    }
  };
};

export default connect(null, mapDispatchToProps)(Container);
