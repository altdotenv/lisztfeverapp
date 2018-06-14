import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";


const PlanDisplay = (props, context) => (
  <div className={styles.container}>
    <div className={styles.column}>
      <img
        src={props.plan.event.eventimageurl ? props.plan.event.eventimageurl : require("images/noPhoto.jpg")}
        alt={props.plan.event.eventname ? props.plan.event.eventname : context.t("No event name")}
        className={styles.bigAvatar}
      />
    </div>
    <div className={styles.column}>
      <a href={`${props.plan.event.primaryeventurl}`} style={{ textDecoration: 'none'}}>
        <div className={styles.event}>
          {props.plan.event.eventstatus ? (
              <div className={styles.eventStatus}>{props.plan.event.eventstatus}</div>
            ) : null
          }
          <div className={styles.eventName}>{props.plan.event.eventname}</div>
          <div className={styles.subInfo}>
            {props.plan.venue.length > 0 ?
              props.plan.venue.map((venue, index) => <Venue venue={venue} key={index} />)
              : (
              <div className={styles.venue}>{context.t("Venue : Not Specified")}</div>
            )}
            <div className={styles.eventDate}>{props.plan.event.eventstartlocaldate}</div>
          </div>
        </div>
      </a>
    </div>
    <div className={styles.column}>
      <button className={styles.button} onClick={props.handleClick}>
        {props.plan.event.is_planned ? context.t("Delete") : context.t("Add")}
      </button>
    </div>
  </div>
)

const Venue = props => (
  <div className={styles.venue}>
    <span className={styles.venue}>{props.venue.venuename} - </span>
    <span className={styles.venue}>{props.venue.venuecity}</span>
  </div>
)

PlanDisplay.contextTypes = {
  t: PropTypes.func.isRequired
}

PlanDisplay.propTypes = {
  plan: PropTypes.shape({
    event: PropTypes.shape({
      eventid: PropTypes.string.isRequired,
      eventname: PropTypes.string.isRequired,
      eventstartlocaldate: PropTypes.string,
      eventimageurl: PropTypes.string.isRequired,
      primaryeventurl: PropTypes.string.isRequired,
      eventstatus: PropTypes.string,
      maxprice: PropTypes.number,
      minprice: PropTypes.number,
      is_planned: PropTypes.bool.isRequired,
    }).isRequired,
    venue: PropTypes.arrayOf(
      PropTypes.shape({
        venueid: PropTypes.string,
        venuename: PropTypes.string,
        venuecity: PropTypes.string,
        venuestreet: PropTypes.string,
      })
    ).isRequired
  }),
  handleClick: PropTypes.func.isRequired
}

export default PlanDisplay;
