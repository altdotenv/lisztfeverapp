import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import Loading from "components/Loading";
import ArtistDisplay from "components/ArtistDisplay";

const Search = (props, context) => {
  if (props.loading) {
    return <LoadingSearch />;
  } else if (!props.loading && props.artistList.length > 0) {
    return <RenderArtistSearch {...props} />;
  } else if (!props.loading && props.artistList.length < 1) {
    return <NotFound text={context.t("Nothing found :(")} />;
  }
};

const LoadingSearch = props => (
  <div className={styles.loading}>
    <Loading />
  </div>
)

const RenderArtistSearch = props => (
  <div className={styles.search}>
    {props.artistList.map(artist => <ArtistDisplay artist={artist} key={artist.artist_id} />)}
  </div>
)

const NotFound = props => <span className={styles.notFound}>{props.text}</span>

Search.contextTypes = {
  t: PropTypes.func.isRequired
}

Search.propTypes = {
  loading: PropTypes.bool.isRequired,
  artistList: PropTypes.array
}

export default Search;
