import React, { useState } from 'react';
import axios from 'axios';
import { Card, CardMedia, Grid, Container, Box, Button, ButtonGroup } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import './LessonThree.css'; 
const LessonThree = () => {
  const [selectedImage, setSelectedImage] = useState('you.jpeg');
  const navigate = useNavigate();

  const handleImageChange = (imageName) => {
    console.log("Changing image to:", imageName); 
    setSelectedImage(imageName);
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

   const handleNavigateToPreviousLesson = () => {
    navigate('/lesson2');
  };

  return (
    <Container className="lesson-container" maxWidth={false} disableGutters>
      <Box sx={{ display: 'flex', justifyContent: 'flex-start', p: 2 }}>
        <Button variant="contained" color="primary" onClick={handleNavigateToPreviousLesson}>
          Previous Lesson
        </Button>
      </Box>

      <Grid container className="lesson-grid">
        <Grid item xs={12} md={6} className="image-container">
          <Card className="lesson-card">
            <CardMedia
              component="img"
              image={`/aslwords/${selectedImage}`}
              alt={selectedImage.split('.')[0]}
            />
          </Card>
        </Grid>
        <Grid item xs={12} md={6} className="real-time-container">
          <Box className="button-container" style={{ display: 'flex', flexDirection: 'column' }}>
            <Button className="real-time-button" onClick={handleStartRecognition} style={{ marginBottom: '10px' }}>
              Start Real-Time Recognition
            </Button>
          </Box>
        </Grid>
      </Grid>

      <Box className="button-box">
        <ButtonGroup variant="text" fullWidth>
          <Button onClick={() => handleImageChange('you.jpeg')}>You</Button>
          <Button onClick={() => handleImageChange('me.jpeg')}>Me</Button>
          <Button onClick={() => handleImageChange('i_love_you.jpeg')}>I Love You</Button>
          <Button onClick={() => handleImageChange('best_of_luck.jpeg')}>Best of Luck</Button>
          <Button onClick={() => handleImageChange('friends.jpeg')}>Friends</Button>
        </ButtonGroup>
      </Box>
    </Container>
  );
};

export default LessonThree;
