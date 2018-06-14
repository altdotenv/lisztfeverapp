import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";
import Loading from "components/Loading";

const ListenMusic = (props, context) => {
  return (
    <div className={styles.listenMusic}>
      {props.loading && <Loading />}
    </div>
  )
};

ListenMusic.contextTypes = {
  t: PropTypes.func.isRequired
}

ListenMusic.propTypes = {
  loading: PropTypes.bool.isRequired,
}

export default ListenMusic;
