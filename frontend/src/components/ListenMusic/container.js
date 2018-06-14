import React, { Component } from "react";
import PropTypes from "prop-types";
import ListenMusic from "./presenter";

class Container extends Component {
  state = {
    loading: true
  }
  static propTypes = {
    redirectListenMusic: PropTypes.func.isRequired
  }
  componentDidMount() {
    const { redirectListenMusic } = this.props;
    redirectListenMusic();
  }
  render(){
    return <ListenMusic {...this.state} />
  }
}

export default Container;
