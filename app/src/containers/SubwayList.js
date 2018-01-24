import React, { Component } from 'react';
import { connect } from 'react-redux';
import Subway from '../components/Subway';
import { fetchSubway } from '../actions/index';

class SubwayList extends Component {
  componentDidMount() {
    this.props.fetchSubway();
  }

  renderSubway () {
    return this.props.subwayList.map((subway) => {
      return <li key={subway.id}><Subway subwayData={subway}/></li>;
    });
  }

  render () {
    return (
      <div>
        <h2>열차 리스트</h2>
        <ul>
          {this.renderSubway()}
        </ul>
      </div>
    );
  }
}

export default connect((state) => {
  return {
    subwayList: state.lists.subwayList
  };
}, { fetchSubway })(SubwayList);