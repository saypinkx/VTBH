import React, { MouseEvent, useState } from 'react';
import { MoreVert } from '@mui/icons-material';
import { IconButton, Menu, MenuItem, Typography } from '@mui/material';
import './header.less';

const menuItems = [
  { id: 'menu-item-upload', value: 'Загрузка' },
  { id: 'menu-item-interactive', value: 'Карта' },
  { id: 'menu-item-logout', value: 'Выйти из системы' },
];

export const Header = (): React.ReactElement => {
  const [anchorEl, setAnchorEl] = useState<HTMLElement | null>(null);

  const handleClickMenu = (event: MouseEvent<HTMLElement>) => setAnchorEl(event.currentTarget);

  const handleCloseMenu = (event: MouseEvent<HTMLElement>) => {
    setAnchorEl(null);
  };

  return (
    <header className="app-header">
      <div className="app-header__logo"></div>
      <Typography variant="body1" component="div" sx={{ flexGrow: 1, textAlign: 'right' }}>
        {'User'}
      </Typography>
      <IconButton
        aria-label="more"
        id="long-button"
        aria-controls="long-menu"
        aria-expanded={!!anchorEl}
        aria-haspopup="true"
        onClick={handleClickMenu}
      >
        <MoreVert/>
      </IconButton>
      <Menu
        id="long-menu"
        MenuListProps={{ 'aria-labelledby': 'long-button' }}
        anchorEl={anchorEl}
        open={!!anchorEl}
        onClose={handleCloseMenu}
      >
        {menuItems.map(option => (
          <MenuItem id={option.id} key={option.id} onClick={handleCloseMenu}>
            {option.value}
          </MenuItem>
        ))}
      </Menu>
    </header>
  )
}
