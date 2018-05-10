import React from 'react';
import PropTypes from "prop-types";
import { Route, Switch } from "react-router-dom";
import './styles.scss';
import Footer from 'components/Footer';
import Auth from "components/Auth";
import Navigation from "components/Navigation";
import Feed from "components/Feed";
import Plan from "components/Plan";
import Search from "components/Search";
import Event from "components/Event";
import SignedRequest from "components/SignedRequest";

const App = props => [
  props.isLoggedIn ? <Navigation key={1}/> : null,
  props.isLoggedIn ? <PrivateRoutes key={2} /> : <PublicRoutes key={2} />,
  <Footer key={3} />
]

App.propTypes = {
  isLoggedIn: PropTypes.bool.isRequired
}

const PrivateRoutes = props => (
  <Switch>
    <Route exact path="/" component={Feed} />
    <Route path="/plan" component={Plan} />
    <Route path="/event/artist/:artistId" component={Event} />
    <Route path="/search/:searchTerm" component={Search} />
  </Switch>
);

const PublicRoutes = props => (
  <Switch>
    <Route exact path="/" component={Auth} />
    <Route exact path="/signed_request/:eventId" component={SignedRequest} />
  </Switch>
);

export default App;
