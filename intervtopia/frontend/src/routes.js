/*!

=========================================================
* Light Bootstrap Dashboard React - v2.0.1
=========================================================

* Product Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/light-bootstrap-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import Dashboard from "views/Dashboard.js";
import Preferences from "views/Preferences.js";
import Friends from "views/Friends.js";
import Messages from "views/Messages.js";
import Evaluations from "views/Evaluations.js";

const dashboardRoutes = [
  {
    path: "/dashboard",
    name: "Dashboard",
    icon: "nc-icon nc-grid-45",
    component: Dashboard,
    layout: "/admin"
  },
  {
    path: "/preferences",
    name: "Preferences",
    icon: "nc-icon nc-settings-gear-64",
    component: Preferences,
    layout: "/admin"
  },
  {
    path: "/friends",
    name: "Friends",
    icon: "nc-icon nc-favourite-28",
    component: Friends,
    layout: "/admin"
  },
  {
    path: "/messages",
    name: "Messages",
    icon: "nc-icon nc-email-85",
    component: Messages,
    layout: "/admin"
  },
  {
    path: "/evaluations",
    name: "Evaluations",
    icon: "nc-icon nc-notes",
    component: Evaluations,
    layout: "/admin"
  }
];

export default dashboardRoutes;
