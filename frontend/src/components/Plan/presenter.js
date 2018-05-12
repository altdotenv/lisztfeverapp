import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import Loading from "components/Loading";
import PlanDisplay from "components/PlanDisplay";

const Plan = (props, context) => {
  if (props.loading) {
    return <LoadingPlan />;
  } else if (!props.loading && props.planList.length > 0) {
    return <RenderPlan {...props} />;
  } else if (!props.loading && props.planList.length < 1) {
    return (
      <NoEvents text={context.t("No Events :(")} />
    )
  }
};

const LoadingPlan = props => (
  <div className={styles.loading}>
    <Loading />
  </div>
)

const RenderPlan = props => (
  <div className={styles.plan}>
    {props.planList.map(plan => (
      <PlanDisplay plan={plan} key={plan.eventid} />
    ))}
  </div>
)

const NoEvents = props => <span className={styles.noEvents}>{props.text}</span>

Plan.contextTypes = {
  t: PropTypes.func.isRequired
}


Plan.propTypes = {
  loading: PropTypes.bool.isRequired,
  planList: PropTypes.array
};

export default Plan;
