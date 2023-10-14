import React from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import { Container, Interactive } from '@src/components';

export const App = (): React.ReactElement => {
  return (
    <Routes>
      <Route element={<Container />}>
        <Route path='/' element={<Interactive />} />
      </Route>
      <Route path='*' element={<Navigate to={'/'} replace />} />
    </Routes>
  );
};
