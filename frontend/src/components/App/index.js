import { connect } from "react-redux";
import Container from "./container";
import { withRouter } from 'react-router-dom';

const mapStateToProps = (state, ownProps) => {
  const { user, routing: { location } } = state;
  console.log(state);
  return {
    isLoggedIn: user.isLoggedIn,
    pathname: location.pathname
  };
}

export default withRouter(connect(mapStateToProps)(Container));
