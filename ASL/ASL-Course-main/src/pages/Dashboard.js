import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Typography, Container, Paper, FormControl, InputLabel, Select, MenuItem, Button } from '@mui/material';
import './Dashboard.css'; 
function Dashboard() {
  const navigate = useNavigate();
  const [level, setLevel] = useState('');

  const handleChange = (event) => {
    setLevel(event.target.value);
  };

  const handleSubmit = () => {
    navigate(`/lesson${level}`);
  };

  return (
    <div className="dashboard-background">
      <Container maxWidth="sm">
        <Paper elevation={3} className="dashboard-card">
          <Typography variant="h4" gutterBottom className="dashboard-heading">
            Welcome to ASL Learning
          </Typography>
          <FormControl variant="outlined" fullWidth className="dashboard-select">
            <InputLabel id="demo-simple-select-outlined-label">Level</InputLabel>
            <Select
              labelId="demo-simple-select-outlined-label"
              id="demo-simple-select-outlined"
              value={level}
              onChange={handleChange}
              label="Level"
            >
              <MenuItem value={1}>One: Alphabets</MenuItem>
              <MenuItem value={2}>Two: Numbers</MenuItem>
              <MenuItem value={3}>Three: Words</MenuItem>
            </Select>
          </FormControl>
          <br/> <br/>
          <Button
            variant="contained"
            fullWidth
            size="large"
            className="dashboard-button"
            onClick={handleSubmit}
          >
            Submit
          </Button>
        </Paper>
      </Container>
    </div>
  );
}

export default Dashboard;
