const CloseWebview = (props, context) => {
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
    window.MessengerExtensions.requestCloseBrowser(function success() {
      // webview closed
    }, function error(err) {
      console.log(err)
    });
  };

  return (null)
}

export default CloseWebview;
