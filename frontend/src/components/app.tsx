import React from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import { Container, Upload } from '@src/components';

export const App = (): React.ReactElement => {
  return (
    <Routes>
      <Route element={<Container />}>
        <Route path='/' element={<Upload />} />
      </Route>
      <Route path='*' element={<Navigate to={'/'} replace />} />
    </Routes>
  );
};
