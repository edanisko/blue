import React, { Component } from "react";
import {
    Route,
    NavLink,
    HashRouter
} from "react-router-dom";
import PrivateRoute from './PrivateRoute';
import Home from "./Home";
import Returns from "./Returns";
import Contact from "./Contact";
import Login from "./Login";
import Signup from './Signup';

class Main extends Component {
    render() {
        return (
            <HashRouter>
                <div>
                    <h1>BlueCargo</h1>
                    <ul className="header">
                        <li><NavLink exact to="/">Home</NavLink></li>
                        <li><NavLink to="/returns">Returns</NavLink></li>
                        <li><NavLink to="/contact">Contact</NavLink></li>
                    </ul>
                    <div className="content">
                        <Route exact path="/" component={Home} />
                        <PrivateRoute path="/returns" component={Returns} />
                        <Route path="/contact" component={Contact} />
                        <Route path="/login" component={Login} />
                        <Route path="/signup" component={Signup} />
                    </div>
                </div>
            </HashRouter>
        );
    }
}

export default Main;