import React, { Component } from "react";
import PropTypes from "prop-types";
import SignedRequest from "./presenter";

class Container extends Component {
  state = {
    loading: true
  }
  static propTypes = {
    redirectSignedRequest: PropTypes.func.isRequired
  }
  componentDidMount() {
    const { redirectSignedRequest } = this.props;
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
          redirectSignedRequest(thread_context['signed_request'])
        },
        function error(err){
          console.log(err)
        }
      );
    };
  }
  render(){
    return <SignedRequest {...this.state} />
  }
}

export default Container;
