import { connect } from "react-redux";
import Container from "./container";
import { push } from "react-router-redux";

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    goToSearch: searchTerm => {
      if (searchTerm[0] === '#'){
        searchTerm = searchTerm.substr(1, ).replace("#", ",")
        dispatch(push(`/search/${searchTerm}`));
      } else {
        alert("Please hashtags!")
      }
    }
  };
};

export default connect(null, mapDispatchToProps)(Container);
