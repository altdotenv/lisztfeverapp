import React, { Component } from "react";
import PropTypes from "prop-types";
import Event from "./presenter";

class Container extends Component {
  state = {
    loading: true
  };
  static propTypes = {
    getEventByArtistId: PropTypes.func.isRequired,
    eventList: PropTypes.array
  };
  componentDidMount() {
    const { getEventByArtistId } = this.props;
    getEventByArtistId();
  }
  componentDidUpdate = (prevProps, prevState) => {
    const { getEventByArtistId } = this.props;
    if(prevProps.match.params !== this.props.match.params) {
      getEventByArtistId();
    }
  }
  componentWillReceiveProps = (nextProps) => {
    if (nextProps.eventList) {
      this.setState({
        loading: false,
        eventList: nextProps.eventList
      });
    }
  }
  render(){
    const { eventList } = this.props;
    return <Event {...this.state} eventList={eventList} />;
  }
}

export default Container;
