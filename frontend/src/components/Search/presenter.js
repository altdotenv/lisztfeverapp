import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import Loading from "components/Loading";
import ArtistDisplay from "components/ArtistDisplay";

const Search = (props, context) => {
  return (
    <div className={styles.search}>
      <div className={styles.section}>
        {props.loading && <Loading />}
        {!props.loading &&
          props.artistList.length < 1 && (
            <NotFound text={context.t("Nothing found :(")} />
          )
        }
        <div className={styles.content}>
          {!props.loading &&
            props.artistList.length > 0 && (
              <RenderArtistSearch artistList={props.artistList} />
            )
          }
        </div>
      </div>
    </div>
  )
};

const RenderArtistSearch = props => props.artistList.map(artist => (
  <ArtistDisplay artist={artist} key={artist.artistid} />
))

const NotFound = props => <span className={styles.notFound}>{props.text}</span>

Search.contextTypes = {
  t: PropTypes.func.isRequired
}

Search.propTypes = {
  loading: PropTypes.bool.isRequired,
  artistList: PropTypes.array
}

export default Search;
