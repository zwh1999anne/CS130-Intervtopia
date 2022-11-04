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
                      <tr>
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
                          You have an upcoming interview with Annie on Oct 10, Monday!
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
                      </tr>
                      <tr>
                        <td>
                          <Form.Check className="mb-1 pl-0">
                            <Form.Check.Label>
                              <Form.Check.Input
                                defaultChecked
                                defaultValue=""
                                type="checkbox"
                              ></Form.Check.Input>
                              <span className="form-check-sign"></span>
                            </Form.Check.Label>
                          </Form.Check>
                        </td>
                        <td className="text-left">
                        You have an evaluation form for Olivia that you interviewed with on Oct 4, Tuesday. 
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
                    <tr>
                      <td>Dakota Rice</td>
                      <td>Sep 26th, Mon, 16:00</td>
                      <td>
                      <div className="text-left">
                          <Button variant="primary" className="btn-fill mr-3" size="sm">
                      Interview Again
                      </Button>{'     '}
                      <Button variant="primary" size="sm">Add Friend</Button>
                      </div>
                      </td>
                    </tr>
                    <tr>
                      <td>Minerva Hooper</td>
                      <td>Sep 30th, Fri, 11:00</td>
                      <td>
                      <div className="text-left">
                          <Button variant="primary" className="btn-fill mr-3" size="sm">
                      Interview Again
                      </Button>{' '}
                      <Button variant="primary" size="sm">Add Friend</Button>
                      </div>
                      </td>
                    </tr>
                    <tr>
                      <td>Sage Rodriguez</td>
                      <td>Oct 3rd, Mon, 9:00</td>
                      <td>
                      <div className="text-left">
                          <Button variant="primary" className="btn-fill mr-3" size="sm">
                      Interview Again
                      </Button>{' '}
                      <Button variant="primary" size="sm">Add Friend</Button>
                      </div>
                      </td>
                    </tr>
                    <tr>
                      <td>Philip Chaney</td>
                      <td>Oct 5th, Wed, 10:00</td>
                      <td>
                      <div className="text-left">
                          <Button variant="primary" className="btn-fill mr-3" size="sm">
                      Interview Again
                      </Button>{' '}
                      <Button variant="primary" size="sm">Add Friend</Button>
                      </div>
                      </td>
                    </tr>
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

export default Dashboard;
