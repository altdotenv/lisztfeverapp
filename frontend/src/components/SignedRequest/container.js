import React, { Component } from "react";
import PropTypes from "prop-types";
import SignedRequest from "./presenter";

class Container extends Component {
  static propTypes = {
    eventSignedRequest: PropTypes.func.isRequired
  }
  componentDidMount() {
    const { eventSignedRequest } = this.props;
    window.fbAsyncInit = function() {
        window.FB.init({
            appId      : '180090909386009',
            autoLogAppEvents : true,
            status     : true,
            cookie     : true,
            version    : 'v2.11',
            xfbml      : true
        });

    };
    // Load the SDK Asynchronously
    (function(d, s, id){
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) {return;}
      js = d.createElement(s); js.id = id;
      js.src = "//connect.facebook.com/en_US/messenger.Extensions.js";
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'Messenger'));

    window.extAsyncInit = function() {
      window.MessengerExtensions.getContext('180090909386009',
        function success(thread_context){
          eventSignedRequest(thread_context['signed_request'])
        },
        function error(err){
          console.log(err)
        }
      );
    };
  }
  componentWillReceiveProps = nextProps => {
    console.log(nextProps)
  }
  render(){
    return <p>signed request</p>
  }
}

export default Container;
