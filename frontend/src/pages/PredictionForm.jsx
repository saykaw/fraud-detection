import React, { useState } from 'react';
import { Box, FormControl, FormLabel, Input, Button, Grid } from "@chakra-ui/react";

function PredictionForm() {
  const [form, setForm] = useState({
    age: '',
    city: '',
    job: '',
    category: '',
    timeOfTransaction: '',
    creditCardNumber: '',
    amount: '',
    merchantLocation: '',
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(form);
  };

  return (
    <Box as="form" p={200} shadow="md" borderWidth="1px" onSubmit={handleSubmit}>
      <Grid templateColumns="repeat(2, 1fr)" gap={6}>
        <FormControl id="age" isRequired>
          <FormLabel>Age</FormLabel>
          <Input name="age" type="number" onChange={handleChange} />
        </FormControl>
        <FormControl id="city" isRequired>
          <FormLabel>City</FormLabel>
          <Input name="city" type="text" onChange={handleChange} />
        </FormControl>
        <FormControl id="job" isRequired>
          <FormLabel>Job</FormLabel>
          <Input name="job" type="text" onChange={handleChange} />
        </FormControl>
        <FormControl id="category" isRequired>
          <FormLabel>Category</FormLabel>
          <Input name="category" type="text" onChange={handleChange} />
        </FormControl>
        <FormControl id="timeOfTransaction" isRequired>
          <FormLabel>Time of Transaction</FormLabel>
          <Input name="timeOfTransaction" type="time" onChange={handleChange} />
        </FormControl>
        <FormControl id="creditCardNumber" isRequired>
          <FormLabel>Credit Card Number</FormLabel>
          <Input name="creditCardNumber" type="text" onChange={handleChange} />
        </FormControl>
        <FormControl id="amount" isRequired>
          <FormLabel>Amount</FormLabel>
          <Input name="amount" type="number" onChange={handleChange} />
        </FormControl>
        <FormControl id="merchantLocation" isRequired>
          <FormLabel>Merchant Location</FormLabel>
          <Input name="merchantLocation" type="text" onChange={handleChange} />
        </FormControl>
      </Grid>
      <Button mt={4} colorScheme="teal" type="submit">
        Submit
      </Button>
    </Box>
  );
}

export default PredictionForm;