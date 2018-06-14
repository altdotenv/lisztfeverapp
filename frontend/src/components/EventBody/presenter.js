import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import EventActions from "components/EventActions";

const EventBody = (props, context) => (
  <div className={styles.container}>
    <div className={styles.column}>
      <img
        src={props.event_image_url ? props.event_image_url : require("images/noPhoto.jpg")}
        alt={props.event_name ? props.event_name : context.t("No event name")}
        className={styles.bigAvatar}
      />
    </div>
    <div className={styles.column}>
      <a href={`${props.primary_event_url}`} style={{ textDecoration: 'none'}}>
        <div className={styles.event}>
          {props.event_status ? (
              <div className={styles.eventStatus}>{props.event_status}</div>
            ) : null
          }
          <div className={styles.eventName}>{props.event_name}</div>
          <div className={styles.subInfo}>
            {props.venues.length > 0 ?
              props.venues.map((venue, index) => <Venue venue={venue} key={index} />)
              : (
                <div className={styles.venue}>{context.t("Venue : Not Specified")}</div>
            )}
            {props.event_start_local_time ? (
              <div className={styles.eventDate}>{props.event_start_local_time} / {props.event_start_local_date}</div>
            ) : (
              <div className={styles.eventDate}>{props.event_start_local_date}</div>
            )}
          </div>
        </div>
      </a>
    </div>
    <div className={styles.column}>
      <EventActions isPlanned={props.is_planned} eventId={props.event_id}/>
    </div>
  </div>
);

const Venue = props => (
  <div className={styles.venue}>
    <span className={styles.venue}>{props.venue.venue_name} - </span>
    <span className={styles.venue}>{props.venue.venue_city}</span>
  </div>
)

EventBody.contextTypes = {
  t: PropTypes.func.isRequired
}

EventBody.proptypes = {
  event_id: PropTypes.string.isRequired,
  event_name: PropTypes.string.isRequired,
  event_start_local_date: PropTypes.string,
  event_start_local_time: PropTypes.string,
  event_image_url: PropTypes.string.isRequired,
  primary_event_url: PropTypes.string.isRequired,
  event_status: PropTypes.string,
  venues: PropTypes.arrayOf(
    PropTypes.shape({
      venue_name: PropTypes.string.isRequired,
      venue_city: PropTypes.string.isRequired,
    })
  ),
  is_planned: PropTypes.bool.isRequired
}

export default EventBody;
