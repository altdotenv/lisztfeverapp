import { connect } from "react-redux";
import { actionCreators as artistActions } from "redux/modules/artists";
import Container from "./container";

const mapStateToProps = (state, ownProps) => {
  const { artists : { artistList }, routing: { location } } = state;
  return {
    artistList,
    location
  }
}

const mapDispatchToProps = (dispatch, ownProps) => {
  const { match: { params: { searchTerm } } } = ownProps;
  return {
    searchByTerm: () => {
      dispatch(artistActions.searchByTerm(searchTerm))
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Container);
