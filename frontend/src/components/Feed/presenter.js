import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import Loading from "components/Loading";
import ArtistDisplay from "components/ArtistDisplay";
import Waypoint from "react-waypoint";

const Feed = (props, context) => {
  return (
    <div className={styles.feed}>
      <div className={styles.section}>
        {props.loading && <Loading />}
        {!props.loading &&
          props.feed.length < 1 && (
            <NotFound text={context.t("Nothing found :(")} />
          )
        }
        <div className={styles.content}>
          {!props.loading &&
            props.feed.length > 0 && (
              <RenderFeed {...props} />
            )
          }
          <Waypoint
            onEnter={props.onEnter}
          />
        </div>
      </div>
    </div>
  )
};

const RenderFeed = props => (
  <div className={styles.feed}>
    {props.feed.map(artist => <ArtistDisplay artist={artist} key={artist.artistid} />)}
  </div>
)

const NotFound = props => <span className={styles.notFound}>{props.text}</span>

Feed.contextTypes = {
  t: PropTypes.func.isRequired
}

Feed.propTypes = {
  loading: PropTypes.bool.isRequired,
  feed: PropTypes.array
};

export default Feed;
