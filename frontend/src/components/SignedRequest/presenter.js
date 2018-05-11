import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import Loading from "components/Loading";

const SignedRequest = (props, context) => {
  return (
    <div className={styles.signedRequest}>
      {props.loading && <Loading />}
    </div>
  )
};

SignedRequest.contextTypes = {
  t: PropTypes.func.isRequired
}

SignedRequest.propTypes = {
  loading: PropTypes.bool.isRequired,
}

export default SignedRequest;
