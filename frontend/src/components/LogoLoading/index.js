import React from "react";
import styles from "./styles.scss";

const LogoLoading = props => (
  <div className={styles.container}>
    <img src={require("images/logo.png")} className={styles.logo} alt="logoloading"/>
  </div>
);

export default LogoLoading;
