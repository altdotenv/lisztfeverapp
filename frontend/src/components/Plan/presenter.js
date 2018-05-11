import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import Loading from "components/Loading";
import PlanDisplay from "components/PlanDisplay";

const Plan = props => {
  if (props.loading) {
    return <LoadingPlan />;
  } else if (props.planList) {
    return <RenderPlan {...props} />;
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

Plan.propTypes = {
  loading: PropTypes.bool.isRequired,
  planList: PropTypes.array
};

export default Plan;
