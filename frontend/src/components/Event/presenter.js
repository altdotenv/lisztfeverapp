import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import Loading from "components/Loading";
import EventBody from "components/EventBody";

const Event = (props, context) => {
  if (props.loading) {
    return <LoadingFeed />;
  } else if (props.eventList.length < 1) {
    return <NotFound text={context.t("No Events :(")} />;
  } else if (props.eventList.length > 0) {
    return <RenderEvent {...props} />;
  }
};

const LoadingFeed = props => (
  <div className={styles.loading}>
    <Loading />
  </div>
);

const RenderEvent = (props, context) => (
  <div className={styles.event}>
  {props.near ? (
    <div className={styles.near}>
      <div className={styles.textNear}>
        <span className={styles.textSpan}>Near You</span>
      </div>
      {props.eventList.map(event => {
        return event.near === 1 ?
          <EventBody {...event} key={event.event_id} />
        : null
      })}
    </div>    
  ) : null}
    <div className={styles.notNear}>
      {props.eventList.map(event => {
        return event.near !== 1 ?
          <EventBody {...event} key={event.event_id} />
        : null
      })}
    </div>
  </div>
);

const NotFound = props => <span className={styles.notFound}>{props.text}</span>;

Event.contextTypes = {
  t: PropTypes.func.isRequired
};

Event.propTypes = {
  loading: PropTypes.bool.isRequired,
  eventList: PropTypes.array
};

export default Event;
