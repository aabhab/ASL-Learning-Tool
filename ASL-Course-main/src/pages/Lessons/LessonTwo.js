import React, { useState } from 'react';
import axios from 'axios';
import { Card, CardMedia, Grid, Container, Box, Button, ButtonGroup } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import './LessonOneTwo.css'; 

const LessonTwo = () => {
  const navigate = useNavigate();
  const [currentLetterIndex, setCurrentLetterIndex] = useState(0);
  const numbers = '0123456789'.split('');

  const handleNavigateToLessonThree = () => {
    navigate('/lesson3');
  };

  const handleNavigateToPreviousLesson = () => {
    navigate('/lesson1');
  };

  const handleStartRecognition = async () => {
    try {
      const response = await axios.post('http://localhost:5000/start-recognition');
      alert('Real-time recognition started successfully.');
      console.log(response.data.message);
    } catch (error) {
      console.error('Error starting real-time recognition:', error);
      alert('Failed to start real-time recognition.');
    }
  };

  return (
    <Container className="lesson-container" maxWidth={false} disableGutters>
      {/* Navigation Buttons */}
      <Box sx={{ display: 'flex', justifyContent: 'space-between', p: 2 }}>
        <Button variant="contained" color="primary" onClick={handleNavigateToPreviousLesson}>
          Previous Lesson
        </Button>
        <Button variant="contained" color="primary" onClick={handleNavigateToLessonThree}>
          Next Lesson
        </Button>
      </Box>

      <Grid container className="lesson-grid">
        <Grid item xs={12} md={6} className="image-container">
          <Box sx={{ width: '100%', padding: '10px' }}>
            <Card className="lesson-card">
              <CardMedia
                component="img"
                image={`/aslletters/${numbers[currentLetterIndex]}.jpeg`} 
                alt={`ASL Sign for ${numbers[currentLetterIndex]}`}
              />
            </Card>
          </Box>
        </Grid>
        <Grid item xs={12} md={6} className="real-time-container">
          <div className="button-container" style={{ display: 'flex', flexDirection: 'column' }}>
            <Button className="real-time-button" onClick={handleStartRecognition} style={{ marginBottom: '10px' }}>
              Start Real-Time Recognition
            </Button>
            
          </div>
        </Grid>
      </Grid>

      <Grid container justifyContent="center" className="letter-grid">
        <ButtonGroup variant="text" aria-label="text button group">
          {numbers.map((number, index) => (
            <Button
              key={number}
              className={`letter-button ${currentLetterIndex === index ? 'active-letter' : ''}`}
              onClick={() => setCurrentLetterIndex(index)}
            >
              {number}
            </Button>
          ))}
        </ButtonGroup>
      </Grid>
    </Container>
  );
};

export default LessonTwo;
