import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";

const Footer = (props, context) => (
  <footer className={styles.footer}>
    <div className={styles.column}>
      <span className={styles.copyright}>&copy; 2018 AREHA.co</span>
    </div>
  </footer>
)

Footer.contextTypes = {
  t: PropTypes.func.isRequired
};

export default Footer;
