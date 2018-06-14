import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import EventBody from "components/EventBody";
import EventActions from "components/EventActions";


const FeedEvent = (props, context) => {
  return (
    <div className={styles.feedEvent}>
      <header>
        <img src={props.event_image_url || require("images/noImage.jpg")} alt={props.event_name} />
      </header>
      <div>
        <EventBody
          eventname={props.event_name}
          eventstatus={props.event_status}
          eventstartlocaldate={props.event_start_local_date}
          artists={props.artists}
          venue={props.venue}
        />
      </div>
      <div>
        <EventActions isPlanned={props.is_planned} eventId={props.eventid}/>
      </div>
    </div>
  )
};

FeedEvent.propTypes = {
  event_id: PropTypes.string.isRequired,
  event_name: PropTypes.string.isRequired,
  event_start_local_date: PropTypes.string,
  event_image_url: PropTypes.string.isRequired,
  primary_event_url: PropTypes.string.isRequired,
  event_status: PropTypes.string,
  venues: PropTypes.arrayOf(
    PropTypes.shape({
      venuename: PropTypes.string.isRequired,
      venuecity: PropTypes.string.isRequired,
    })
  ),
  is_planned: PropTypes.bool.isRequired
}

export default FeedEvent;
