import React from "react";

// react-bootstrap components
import {
  Badge,
  Button,
  Card,
  Form,
  Navbar,
  Nav,
  Container,
  Row,
  Col
} from "react-bootstrap";

import default_preferences from "backend_data/default_preferences";

function Preferences() {
  return (
    <>
      <Container fluid>
        <Row>
          <Col md="12">
            <Card>
              <Card.Header>
                <Card.Title as="h4">Edit Preferences</Card.Title>
              </Card.Header>
              <Card.Body>
                <Form>
                  <Row>
                    <Col className="pr-1" md="3">
                      <Form.Group>
                        <label>Username</label>
                        <Form.Control
                          defaultValue={default_preferences.username}
                          placeholder="Your Username"
                          type="text"
                        ></Form.Control>
                      </Form.Group>
                    </Col>
                    <Col className="px-1" md="5">
                      <Form.Group>
                        <label>Education</label>
                        <Form.Control
                          defaultValue={default_preferences.school}
                          placeholder="Which University are you attending? What's your major?"
                          type="text"
                        ></Form.Control>
                      </Form.Group>
                    </Col>
                    <Col className="pl-1" md="4">
                      <Form.Group>
                        <label htmlFor="exampleInputEmail1">
                          Email address
                        </label>
                        <Form.Control
                          defaultValue={default_preferences.email}
                          placeholder="Email"
                          type="email"
                        ></Form.Control>
                      </Form.Group>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-1" md="4">
                      <Form.Group>
                        <Form.Label>Select the job role you are seeking</Form.Label>
                        <br />
                        <Form.Select
                          defaultValue={default_preferences.job_role} className="w-100 form-control">
                          <option value="software engineer">Software Engineer</option>
                          <option value="data scientist">Data Scientist</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                    <Col className="pl-1" md="4">
                      <Form.Group>
                      <Form.Label>Select your desired interview role</Form.Label>
                        <br />
                        <Form.Select
                          defaultValue={default_preferences.interview_role}  className="w-100 form-control">
                          <option value="interviewee">Interviewer</option>
                          <option value="interviewer">Interviewee</option>
                          <option value="both">Both</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                    <Col className="pl-1" md="4">
                      <Form.Group>
                      <Form.Label>Select your desired interview difficulty</Form.Label>
                        <br />
                        <Form.Select
                          defaultValue={default_preferences.desired_difficulty} className="w-100 form-control" >
                          <option value="easy">Easy</option>
                          <option value="medium">Medium</option>
                          <option value="hard">Hard</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                  </Row>
                  <Row>
                    <Col md="6">
                    <Form.Group>
                      <Form.Label>Select your favorite programming language</Form.Label>
                        <br />
                        <Form.Select
                          defaultValue={default_preferences.first_language} className="w-100 form-control" >
                          <option value="C++">C++</option>
                          <option value="Java">Java</option>
                          <option value="JavaScript">JavaScript</option>
                          <option value="Python">Python</option>
                          <option value="Go">Go</option>
                          <option value="SQL">SQL</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                    <Col md="6">
                    <Form.Group>
                      <Form.Label>Select your second favorite programming language</Form.Label>
                        <br />
                        <Form.Select
                          defaultValue={default_preferences.second_language} className="w-100 form-control" >
                          <option value="C++">C++</option>
                          <option value="Java">Java</option>
                          <option value="JavaScript">JavaScript</option>
                          <option value="Python">Python</option>
                          <option value="Go">Go</option>
                          <option value="SQL">SQL</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                  </Row>
                  <Row>
                  <Col md="6">
                    <Form.Group>
                      <Form.Label>Select your available day</Form.Label>
                        <br />
                        <Form.Select
                          defaultValue={default_preferences.available_day} className="w-100 form-control" >
                          <option value="Monday">Monday</option>
                          <option value="Tuesday">Tuesday</option>
                          <option value="Wednesday">Wednesday</option>
                          <option value="Thursday">Thursday</option>
                          <option value="Friday">Friday</option>
                          <option value="Saturday">Saturday</option>
                          <option value="Sunday">Sunday</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                    <Col md="6">
                    <Form.Group>
                      <Form.Label>Select your available time slot</Form.Label>
                        <br />
                        <Form.Select
                          defaultValue={default_preferences.available_time} className="w-100 form-control" >
                          <option value="9:00 - 10:00 A.M.">9:00 - 10:00 A.M.</option>
                          <option value="10:00 - 11:00 A.M.">10:00 - 11:00 A.M.</option>
                          <option value="11:00 - 12:00 P.M.">11:00 - 12:00 P.M.</option>
                          <option value="12:00 - 1:00 P.M.">12:00 - 1:00 P.M</option>
                          <option value="1:00 - 2:00 P.M.">1:00 - 2:00 P.M</option>
                          <option value="2:00 - 3:00 P.M.">2:00 - 3:00 P.M.</option>
                          <option value="3:00 - 4:00 P.M.">3:00 - 4:00 P.M</option>
                          <option value="4:00 - 5:00 P.M.">4:00 - 5:00 P.M</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                  </Row>
                  <Row>
                  <Col md="6">
                    <Form.Group>
                      <Form.Label>Select your additional available day</Form.Label>
                        <br />
                        <Form.Select
                          defaultValue={default_preferences.additional_available_day} className="w-100 form-control" >
                          <option value="Monday">Monday</option>
                          <option value="Tuesday">Tuesday</option>
                          <option value="Wednesday">Wednesday</option>
                          <option value="Thursday">Thursday</option>
                          <option value="Friday">Friday</option>
                          <option value="Saturday">Saturday</option>
                          <option value="Sunday">Sunday</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                    <Col md="6">
                    <Form.Group>
                      <Form.Label>Select your available time slot</Form.Label>
                        <br />
                        <Form.Select
                          defaultValue={default_preferences.additional_available_time} className="w-100 form-control" >
                          <option value="9:00 - 10:00 A.M.">9:00 - 10:00 A.M.</option>
                          <option value="10:00 - 11:00 A.M.">10:00 - 11:00 A.M.</option>
                          <option value="11:00 - 12:00 P.M.">11:00 - 12:00 P.M.</option>
                          <option value="12:00 - 1:00 P.M.">12:00 - 1:00 P.M</option>
                          <option value="1:00 - 2:00 P.M.">1:00 - 2:00 P.M</option>
                          <option value="2:00 - 3:00 P.M.">2:00 - 3:00 P.M.</option>
                          <option value="3:00 - 4:00 P.M.">3:00 - 4:00 P.M</option>
                          <option value="4:00 - 5:00 P.M.">4:00 - 5:00 P.M</option>
                        </Form.Select>
                      </Form.Group>
                    </Col>
                  </Row>
                  <Button
                    className="btn-fill pull-right mt-5"
                    type="submit"
                    variant="primary"
                  >
                    Update Preferences
                  </Button>
                  <div className="clearfix"></div>
                </Form>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default Preferences;
