import React, { Component } from "react";
import PropTypes from "prop-types";
import Feed from "./presenter";

// fix key duplicate when scrolling

class Container extends Component {
  state = {
    loading: true
  };
  static propTypes = {
    getFeed: PropTypes.func.isRequired,
    feed: PropTypes.array
  };
  componentDidMount() {
    const { getFeed } = this.props;
    if(this.props.feed.length < 1){
      getFeed();
    } else {
      this.setState({
        loading: false
      });
    }

  }

  componentWillReceiveProps = (nextProps, nextState) => {
    if (nextProps.feed) {
      this.setState({
        loading: false,
        feed: nextProps.feed
      });
    }
  }

  render(){
    const { feed } = this.props;
    return <Feed {...this.state} feed={feed} />;
  }
}

export default Container;

// class Container extends Component {
//   state = {
//     loading: true,
//     page: 1
//   };
//   static propTypes = {
//     getFeed: PropTypes.func.isRequired,
//     total_pages: PropTypes.number,
//     feed: PropTypes.array
//   };
//   componentDidMount() {
//     const { getFeed } = this.props;
//     const { page } = this.state.page;
//     if(this.props.feed.length < 1){
//       getFeed(page);
//     } else {
//       this.setState({
//         loading: false
//       });
//     }
//
//   }
//
//   componentWillReceiveProps = (nextProps, nextState) => {
//     if (nextProps.feed) {
//       this.setState({
//         loading: false,
//         feed: nextProps.feed
//       });
//     }
//   }
//
//   render(){
//     const { feed } = this.props;
//     return <Feed {...this.state} feed={feed} onEnter={this._onEnter}/>;
//   }
//   _onEnter = event => {
//     const { getFeed } = this.props;
//     if(event['event'] && this.props.total_pages > this.state.page){
//       this.setState({
//         page: this.state.page +=1
//       })
//       getFeed(this.state.page)
//     }
//   }
// }
