import React, { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

const UserProfile = () => {
    const { user } = useContext(AuthContext);
    
    return (
      <div>
        <Typography variant="h6">
          Welcome, {user.username}
        </Typography>
        <Typography variant="body1">
          Email: {user.email}
        </Typography>
        <Button variant="contained" color="primary" onClick={() => logout()}>
          Logout
        </Button>
      </div>
    );
  };

  export default UserProfile