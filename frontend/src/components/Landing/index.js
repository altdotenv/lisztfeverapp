import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";

const Landing = (props, context) => (
  <main className={styles.landing}>
    <section className={styles.landingFull}>
      <div className={styles.landingMain__logo}>
        <img src={require("images/logo.png")} alt={context.t("Logo")}/>
      </div>
      <div className={styles.landingMain__caption}>"Always Live in Concerts"</div>
      <div className={styles.landingMain__msgus}>
        <a href="http://m.me/lisztfever" className={styles.buttonSend}>
          <img src={require("images/ic_send_med_white.png")} alt={context.t("Send button")}/>
          <span>Send to Messenger</span>
        </a>
      </div>
    </section>
    <section className={styles.landingPartition}>

    </section>
  </main>
)

Landing.contextTypes = {
  t: PropTypes.func.isRequired
};

export default Landing;
