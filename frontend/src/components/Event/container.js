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
    if (prevProps.match.params.artistId !== this.props.match.params.artistId) {
      getEventByArtistId();
    }
  };
  componentWillReceiveProps = nextProps => {
    if (nextProps.eventList) {
      this.setState({
        loading: false,
        eventList: nextProps.eventList
      });
    }
  };
  render() {
    const { eventList } = this.props;
    const nearBool = this._nearBool();
    return <Event {...this.state} eventList={eventList} near={nearBool}/>;
  }
  _nearBool = () => {
    const { eventList } = this.props;
    if(eventList){
      for (var i=0; i<=eventList.length; i++){
        if(eventList[i].near === 1){
          return true
        } else {
          return false
        }
      };
    }
  }
}

export default Container;
