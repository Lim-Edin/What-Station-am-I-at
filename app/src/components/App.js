import React, { Component } from 'react';
import { NavLink, Route, Switch } from 'react-router-dom'
import Home from './Home'
import SubwayList from '../containers/SubwayList'

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h1>어느 역에 있지?</h1>
        </div>
        <div className="content-wrapper">
          <ul>
            <li><NavLink exact to="/">홈으로</NavLink></li>
            <li><NavLink to="/moim">열차 리스트</NavLink></li>
          </ul>
        <Switch>
          <Route exact path="/moim" component={SubwayList}/>
          <Route exact path="/" component={Home}/>
        </Switch>
      </div>
      </div>
    );
  }
}

export default App;