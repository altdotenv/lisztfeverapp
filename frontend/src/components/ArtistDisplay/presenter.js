import React from "react";
import PropTypes from "prop-types";
import { Link } from  "react-router-dom";
import Ionicon from "react-ionicons";
import styles from "./styles.scss";


const ArtistDisplay = (props, context) => (
    <div className={styles.container}>
      <div className={styles.column}>
        <img
          src={props.artist.image_url || require("images/noImage.jpg")}
          alt={props.artist.artist_name || context.t("No artist")}
          className={styles.bigAvatar}
        />
      </div>
      <div className={styles.column}>
        <div className={styles.artist}>
          <Link to={`/event/artist/${props.artist.artist_id}`} style={{ textDecoration: 'none'}}>
            <div className={styles.artistName}>{props.artist.artist_name}</div>
          </Link>
          {props.artist.genres.length > 0 ? (
            <Genre {...props} />
          ) : null}
          {props.artist.local_count ? (
            props.artist.total_count > 1 ? (
              <div className={styles.eventCount}>{props.artist.total_count} Total Events / {props.artist.local_count} Near You</div>
            ) : (
              <div className={styles.eventCount}>{props.artist.total_count} Total Event / {props.artist.local_count} Near You</div>
            )
          ) : (
            props.artist.total_count > 1 ? (
              <div className={styles.eventCount}>{props.artist.total_count} Total Events</div>
            ) : (
              <div className={styles.eventCount}>{props.artist.total_count} Total Event</div>
            )
          )}
        </div>
      </div>
      <div className={styles.column}>
        <div className={styles.artistButton}>
          <Link to={`/event/artist/${props.artist.artist_id}`}>
            <Ionicon icon="ios-pricetags-outline" fontSize="28px" color="#e83862"/>
          </Link>
        </div>
        <div className={styles.artistButton}>
          <Link to={`/listen/${props.artist.artist_id}`}>
            <Ionicon icon="ios-headset-outline" fontSize="28px" color="#e83862"/>
          </Link>
        </div>
      </div>
    </div>
  )

const Genre = props => (
  <div className={styles.genres}>
    {props.artist.genres.map(genre =>(
      <Link to={`/search/${genre}`} style={{ textDecoration: 'none'}} key={genre}>
        <span className={styles.genre}>#{genre} </span>
      </Link>
    ))}
  </div>
)


ArtistDisplay.propTypes = {
  artist: PropTypes.shape({
    artist_id: PropTypes.string.isRequired,
    artist_name: PropTypes.string.isRequired,
    popularity: PropTypes.number.isRequired,
    image_url: PropTypes.string,
    genres: PropTypes.array,
    total_count: PropTypes.number,
    local_count: PropTypes.number
  })
};

export default ArtistDisplay;
