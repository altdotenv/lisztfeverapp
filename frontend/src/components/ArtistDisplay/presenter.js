import React from "react";
import PropTypes from "prop-types";
import { Link } from  "react-router-dom";
import Ionicon from "react-ionicons";
import styles from "./styles.scss";


const ArtistDisplay = (props, context) => {
  return (
    <div className={styles.artistDisplay}>
      <header>
        <img src={props.artist.imageurl || require("images/noImage.jpg")} alt={props.artist.artistname} />
      </header>
      <div className={styles.artistBody}>
        <span className={styles.artistName}>{props.artist.artistname}</span>
        <span className={styles.text}>{props.artist.popularity}</span>
      </div>
      <div>
        <ArtistActions artistid={props.artist.artistid}/>
      </div>
    </div>
  )
};

// const Genre = props => (
//     <span>#{props.genre.genre}</span>
// )

const ArtistActions = props => (
  <div className={styles.actions}>
    <div className={styles.artistIcon}>
      <Link to={`/event/artist/${props.artistid}`}>
        <Ionicon icon="ios-pricetags-outline" fontSize="28px" color="black"/>
      </Link>
    </div>
    <div className={styles.artistIcon}>
      <Link to={`/listen/${props.artistid}`}>
        <Ionicon icon="ios-headset-outline" fontSize="28px" color="black"/>
      </Link>
    </div>
  </div>
)


ArtistDisplay.propTypes = {
  artist: PropTypes.shape({
    artistid: PropTypes.string.isRequired,
    artistname: PropTypes.string.isRequired,
    popularity: PropTypes.number.isRequired,
    imageurl: PropTypes.string,
  })
};

export default ArtistDisplay;
