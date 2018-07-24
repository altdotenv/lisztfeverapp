import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";

const NotFound = (props, context) => (
  <main className={styles.notFound}>
    <div className={styles.column}>
      <div className={styles.notFound__error}>404 Error</div>
      <div className={styles.notFound__text}>Pages Not Found...</div>
    </div>
    <div className={styles.column}>
      <a href="/" className={styles.button}>Back to Home</a>
    </div>
  </main>
)

NotFound.contextTypes = {
  t: PropTypes.func.isRequired
};

export default NotFound;
