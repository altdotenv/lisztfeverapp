import React from "react";
import PropTypes from "prop-types";
import Ionicon from "react-ionicons";
import styles from "./styles.scss";

const EventActions = (props, context) => (
  <div className={styles.actions}>
    <span className={styles.icon} onClick={props.handleCalendarClick}>
      {props.isPlanned ? (
        <Ionicon icon="ios-calendar" fontSize="28px" color="#e83862"/>
      ) : (
        <Ionicon icon="ios-calendar-outline" fontSize="28px" color="#e83862"/>
      )}
    </span>
  </div>
)

EventActions.propTypes = {
  isPlanned: PropTypes.bool.isRequired,
  eventId: PropTypes.string.isRequired,
  handleCalendarClick: PropTypes.func.isRequired
}

export default EventActions;
