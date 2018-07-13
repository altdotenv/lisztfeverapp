import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";

const Footer2 = (props, context) => (
  <footer className={styles.footer}>
    <div className={styles.row}>
      <div className={styles.column}>
        <img src={require("images/logo.png")} alt={context.t("Logo")}/>
      </div>
      <div className={styles.column}>
        <a href="https://www.facebook.com/lisztfever/">
          <i className="fab fa-facebook-square fa-2x"></i>
        </a>
        <a href="https://www.instagram.com/lisztfever_official/">
          <i className="fab fa-instagram fa-2x"></i>
        </a>
      </div>
    </div>
    <div className={styles.row}>
      <div className={styles.column}><span className={styles.copyright}>&copy; 2018 AREHA CO.</span></div>
      <div className={styles.column}>
        <a href="/terms">Terms of Service</a>
        <a href="/policy">Privacy Policy</a>
      </div>
    </div>
  </footer>
)

Footer2.contextTypes = {
  t: PropTypes.func.isRequired
};

export default Footer2;
