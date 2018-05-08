import React from "react";
import { actionCreators as userActions } from "redux/modules/user";

const SignedRequest = () => {
  (function(d, s, id){
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) {return;}
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/messenger.Extensions.js";
  fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'Messenger'));

  MessengerExtensions.getContext('180090909386009',
    function success(thread_context){
      console.log(thread_context.signed_request)
    },
    function error(err){
      console.log(err)
    }
  );
}

export default SignedRequest;
