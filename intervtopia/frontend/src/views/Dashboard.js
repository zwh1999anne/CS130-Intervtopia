import React from "react";
import ChartistGraph from "react-chartist";
// react-bootstrap components
import {
  Badge,
  Button,
  Card,
  Navbar,
  Nav,
  Table,
  Container,
  Row,
  Col,
  Form,
  OverlayTrigger,
  Tooltip,
} from "react-bootstrap";

import toDos from "backend_data/to_do_list";
import interviews_list from "backend_data/interviews_list";

function Dashboard() {
  return (
    <>
      <Container fluid>
        <Row>
          <Col md="8">
          <Card className="card-tasks">
              <Card.Header>
                <Card.Title as="h4">To-do List</Card.Title>
              </Card.Header>
              <Card.Body>
                <div className="table-full-width">
                  <Table>
                    <tbody>
                    {
                      toDos.map((element, index) => {
                          if(element.type === "interview"){
                            return <tr key={index}>
                            <td>
                              <Form.Check className="mb-1 pl-0">
                                <Form.Check.Label>
                                  <Form.Check.Input
                                    defaultValue=""
                                    type="checkbox"
                                  ></Form.Check.Input>
                                  <span className="form-check-sign"></span>
                                </Form.Check.Label>
                              </Form.Check>
                            </td>
                            <td className="text-left">
                              <div>
                              You have an upcoming interview with {element.name} on {element.time}!
                              </div>
                              <div className="text-left">
                              <Button variant="primary" className="btn-fill mr-5" size="sm">
                          Cancel
                          </Button>{' '}
                          <Button variant="primary" className="mr-5" size="sm">Reschedule</Button>{' '}
                          <Button variant="outline-secondary" size="sm">View Profile</Button>
                              </div>
                            </td>
                            <td className="td-actions text-right">
                              <OverlayTrigger
                                overlay={
                                  <Tooltip id="tooltip-506045838">Remove this task!</Tooltip>
                                }
                              >
                                <Button
                                  className="btn-simple btn-link p-1"
                                  type="button"
                                  variant="danger"
                                >
                                  <i className="fas fa-times"></i>
                                </Button>
                              </OverlayTrigger>
                            </td>
                          </tr>;
                          }
                          else{
                            return <tr key={index}>
                            <td>
                              <Form.Check className="mb-1 pl-0">
                                <Form.Check.Label>
                                  <Form.Check.Input
                                    defaultValue=""
                                    type="checkbox"
                                  ></Form.Check.Input>
                                  <span className="form-check-sign"></span>
                                </Form.Check.Label>
                              </Form.Check>
                            </td>
                            <td className="text-left">
                            You have an evaluation form for {element.name} that you interviewed with on {element.time}. 
                            <div className="text-left">
                              <Button variant="primary" className="btn-fill mr-5" size="sm">
                          Evaluate
                          </Button>{' '}
                          <Button variant="primary" className="mr-5" size="sm">Add Friend</Button>{' '}
                          <Button variant="outline-secondary" size="sm">View Profile</Button>
                              </div>
                            </td>
                            <td className="td-actions text-right">
                              <OverlayTrigger
                                overlay={
                                  <Tooltip id="tooltip-21130535">Remove this task!</Tooltip>
                                }
                              >
                                <Button
                                  className="btn-simple btn-link p-1"
                                  type="button"
                                  variant="danger"
                                >
                                  <i className="fas fa-times"></i>
                                </Button>
                              </OverlayTrigger>
                            </td>
                          </tr>
                          }
                      })
                    }
                    </tbody>
                  </Table>
                </div>
              </Card.Body>
            </Card>
          </Col>
          <Col md="4">
            <Card className="text-center">
              <Card.Header>
                <Card.Title as="h4">Do you want to launch a new interview?</Card.Title>
              </Card.Header>
              <Card.Body>
              <p className="description text-center">
               You could choose to be randomly matched with a peer, <br></br>
               matched within your history, 
               or invite a friend!
              </p>
              <Button variant="primary" className="btn-fill">
              Add New Match
              </Button>
              </Card.Body>
            </Card>
          </Col>
        </Row>
        <Row>
          <Col md="12">
            <Card className="card-tasks">
              <Card.Header>
                <Card.Title as="h4">Recent Interviews</Card.Title>
              </Card.Header>
              <Card.Body>
              <Table className="table-hover table-striped">
                  <thead>
                    <tr>
                      <th className="border-0">Match Name</th>
                      <th className="border-0">Interview Time</th>
                      <th className="border-0">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                  {
                    interviews_list.map((element, index) => {
                      return <tr key={index}>
                         <td>{element.name}</td>
                        <td>{element.time}</td>
                        <td>
                        <div className="text-left">
                        <Button variant="primary" className="btn-fill mr-3" size="sm">
                        Interview Again
                        </Button>{'     '}
                        <Button variant="primary" size="sm">Add Friend</Button>
                        </div>
                        </td>
                        </tr>;
                    })
                  }
                  </tbody>
                </Table>
              </Card.Body>
              <Card.Footer>
              </Card.Footer>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
}
import interviews from "backend_data/interviews_list";

export default Dashboard;
