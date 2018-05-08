import React, { Component } from "react";
import PropTypes from "prop-types";
import Plan from "./presenter";

class Container extends Component {
  state = {
    loading: true
  };
  static propTypes = {
    getEventPlans: PropTypes.func.isRequired,
    planList: PropTypes.array
  };

  componentDidMount(){
    const { getEventPlans } = this.props;
    getEventPlans();
  }

  componentWillReceiveProps = nextProps => {
    if (nextProps.planList) {
      this.setState({
        loading: false,
        planList: nextProps.planList
      });
    }
  };
  render() {
    const { planList } = this.props;
    return <Plan {...this.state} planList={ planList }/>
  }
}

export default Container;
