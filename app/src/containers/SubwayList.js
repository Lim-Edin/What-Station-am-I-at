import React, { Component } from 'react';
import { connect } from 'react-redux';
import Subway from '../components/Subway';
import { fetchSubway } from '../actions/index';

class SubwayList extends Component {
  componentDidMount() {
    this.props.fetchSubway(); //이 액션으로 api로부터 데이터를 GET
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
            { alert("열차리스트") }
        </ul>
      </div>
    );
  }
}

export default connect((state) => {
  return {
    subwayList: state.lists.subwayList // GET한 데이터를 subwayList에 저장
  };
}, { fetchSubway })(SubwayList);