import React from "react";
import PropTypes from "prop-types";
import { Route, Switch } from "react-router-dom";
import "./styles.scss";
import Footer from "components/Footer";
import Footer2 from "components/Footer2";
import Navigation from "components/Navigation";
import Feed from "components/Feed";
import Plan from "components/Plan";
import Search from "components/Search";
import Event from "components/Event";
import Landing from "components/Landing";
import SignedRequest from "components/SignedRequest";
import ListenMusic from "components/ListenMusic";
import CloseWebview from "components/CloseWebview";

const App = props => [
  props.pathname === '/' ? null : props.isLoggedIn ? <Navigation key={1} /> : null,
  props.isLoggedIn ? <PrivateRoutes key={2} /> : <PublicRoutes key={2} />,
  props.pathname === '/' ? <Footer2 key={3} /> : props.isLoggedIn ? <Footer key={3} /> : <Footer2 key={3} />
];

App.propTypes = {
  isLoggedIn: PropTypes.bool.isRequired
};

const PrivateRoutes = props => (
  <Switch>
    <Route exact path="/" component={Landing} />
    <Route exact path="/plan" component={Plan} />
    <Route exact path="/feed" component={Feed} />
    <Route exact path="/event/artist/:artistId" component={Event} />
    <Route exact path="/search/:searchTerm" component={Search} />
    <Route exact path="/signed_request/plan" component={Plan} />
    <Route exact path="/signed_request/feed" component={Feed} />
    <Route
      exact
      path="/signed_request/event/artist/:artistId"
      component={Event}
    />
    <Route exact path="/listen/:artistId" component={ListenMusic} />
    <Route exact path="/close/browser" component={CloseWebview} />
  </Switch>
);

const PublicRoutes = props => (
  <Switch>
    <Route exact path="/" component={Landing} />
    <Route exact path="/signed_request/:path" component={SignedRequest} />
    <Route
      exact
      path="/signed_request/event/artist/:artistId"
      component={SignedRequest}
    />
  </Switch>
);

export default App;
