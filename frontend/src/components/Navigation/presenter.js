import React from "react";
import PropTypes from "prop-types";
import Ionicon from "react-ionicons";
import { Link } from  "react-router-dom";
import styles from "./styles.scss";

const Navigation = (props, context) => (
  <div className={styles.navigation}>
    <div className={styles.inner}>
      <div className={styles.column}>
        <Link to="/">
          <img src={require("images/logo.png")} className={styles.logo} alt={context.t("Logo")}/>
        </Link>
      </div>
      <div className={styles.column}>
        <form onSubmit={props.onSubmit}>
          <input
            type="text"
            placeholder={context.t("#genre")}
            className={styles.searchInput}
            onChange={props.onInputChange}
            value={props.value}
          />
        </form>
      </div>
      <div className={styles.column}>
        <div className={styles.navIcon}>
          <Link to="/plan">
            <Ionicon icon="ios-calendar-outline" fontSize="28px" color="#e83862"/>
          </Link>
        </div>
      </div>
    </div>
  </div>
)

Navigation.contextTypes = {
  t: PropTypes.func.isRequired
}

Navigation.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  onInputChange: PropTypes.func.isRequired,
  value: PropTypes.string.isRequired
}
export default Navigation;
