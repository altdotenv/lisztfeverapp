import React, { Component } from "react";
import PropTypes from "prop-types";
import Search from "./presenter";

class Container extends Component {
  state = {
    loading: true
  };
  static propTypes = {
    searchByTerm: PropTypes.func.isRequired,
    artistList: PropTypes.array
  }
  componentDidMount(){
    const { searchByTerm } = this.props;
    searchByTerm();
  }
  componentDidUpdate = (prevProps, prevState) => {
    const { searchByTerm } = this.props;
    if(this.props.match.params.searchTerm !== prevProps.match.params.searchTerm){
      this.setState({
        loading: true
      })
      searchByTerm();
    }
  }
  componentWillReceiveProps(nextProps, nextState) {
    if(nextProps.artistList){
      this.setState({
        loading: false
      })
    }
  }

  render() {
    const { artistList } = this.props;
    return <Search {...this.state} artistList={artistList} />;
  }
}

export default Container;
