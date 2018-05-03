import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import Loading from "components/Loading";
import FeedEvent from "components/FeedEvent";

const Event = (props, context) => {
  if (props.loading) {
    return <LoadingFeed />;
  } else if (props.eventList.length < 1) {
    return <NotFound text={context.t("No Events :(")} />;
  } else if(props.eventList.length >0 ) {
    return <RenderFeed {...props} />;
  }
};

const LoadingFeed = props => (
  <div className={styles.event}>
    <Loading />
  </div>
)

const RenderFeed = props => (
  <div className={styles.event}>
    {props.eventList.map(event => <FeedEvent {...event} key={event.eventid} />)}
  </div>
)

const NotFound = props => <span className={styles.notFound}>{props.text}</span>

Event.contextTypes = {
  t: PropTypes.func.isRequired
}

Event.propTypes = {
  loading: PropTypes.bool.isRequired,
  eventList: PropTypes.array
};

export default Event;
