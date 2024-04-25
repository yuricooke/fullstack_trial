import React from 'react';
import { useNavigate } from 'react-router-dom';
import UserContext from '../api/UserContext';


const RegistrationForm = ({ postUser }) => {
  const navigate = useNavigate();
  const { setUser } = React.useContext(UserContext); // Acessando setUser do UserContext

  const handleSubmit = async (event) => {
    event.preventDefault();
    const nome = event.target.elements.nome.value;
    const email = event.target.elements.email.value;
    
    if (!nome.trim() || !email.trim()) {
      alert('Please enter both name and email.');
      return;
    }
    
    try {
      const response = await postUser(nome, email);
      console.log('User registered successfully:', response);
      // Update user state with id, name, and email
      setUser({ id: response.id, nome, email });
      navigate("/Hikes");
    } catch (error) {
      console.error('Error registering user:', error);
      alert('Failed to register user. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="nome"
          required
        />
      </div>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          required
        />
      </div>
      <button
        type="submit"
        className="btn btn-dark btn-lg rounded-pill more-info my-3"
      >
        Let's Hike!
      </button>
    </form>
  );
};

export default RegistrationForm;
