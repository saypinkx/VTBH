import React, { useEffect, useRef, useState } from 'react';
import {Box, Button, Checkbox, FormControlLabel, FormGroup, Grid, Tab, Tabs} from '@mui/material';
import { filterAtm } from '@src/api';
import { YMap } from '@yandex/ymaps3-types';
import './interactive.less';

let DefaultMarker;
let map: YMap = null;

async function main(): Promise<void> {
  await ymaps3.ready;
  const { YMap, YMapDefaultFeaturesLayer, YMapDefaultSchemeLayer, YMapControls } = ymaps3;
  const { YMapZoomControl } = await ymaps3.import('@yandex/ymaps3-controls@0.0.1');
  DefaultMarker = (await ymaps3.import('@yandex/ymaps3-markers@0.0.1')).YMapDefaultMarker;
  map = new YMap(document.getElementById('root'), { location: { center: [37.623082, 55.75254], zoom: 10 } });
  map.addChild(new YMapDefaultSchemeLayer({}));
  map.addChild(new YMapControls({ position: 'right' }).addChild(new YMapZoomControl({})));
  map.addChild(new YMapDefaultFeaturesLayer({}));
}

export const Interactive = (): React.ReactElement => {
  const initialized = useRef(false);
  const [activeTab, setActiveTab] = useState(0);
  const [isAllDay, setIsAllDay] = useState(false);
  const [wheelchair, setWheelchair] = useState(false);
  const [blind, setBlind] = useState(false);
  const [nfc, setNfc] = useState(false);
  const [qrRead, setQrRead] = useState(false);
  const [usd, setUsd] = useState(false);
  const [chargeRub, setChargeRub] = useState(false);
  const [eur, setEur] = useState(false);
  const [rub, setRub] = useState(false);

  const getAtms = async (): Promise<void> => {
    try {
      const result = await filterAtm({
        is_all_day: isAllDay,
        wheelchair,
        blind,
        nfc_for_bank_cards: nfc,
        qr_read: qrRead,
        supports_usd: usd,
        supports_charge_rub: chargeRub,
        supports_eur: eur,
        supports_rub: rub,
      });
      console.log(result);
    } catch (e) {
      console.error(e);
    }
  };

  useEffect(() => {
    if (!initialized.current) {
      initialized.current = true;
      getAtms().catch(console.log);
      main();
    }
    return () => map?.destroy();
  }, []);

  return (
    <Grid container sx={{ width: '100%', minWidth: 768, height: '100%' }} wrap="nowrap">
      <Grid className="info" item>
        <div className="scrollable">
          {
            <>
              <Box sx={{ borderBottom: 1, borderColor: 'divider', marginBottom: '1rem' }}>
                <Tabs onChange={(_, index) => setActiveTab(index)} value={activeTab} variant="fullWidth">
                  <Tab label="Банкоматы" />
                  <Tab label="Офисы" />
                </Tabs>
              </Box>
              <Box component="div" sx={{ display: activeTab === 0 ? 'block' : 'none', marginLeft: 1 }}>
                <FormGroup>
                  <FormControlLabel
                    control={<Checkbox checked={isAllDay} onChange={e => setIsAllDay(e.target.checked)} />}
                    label="Весь день"
                  />
                  <FormControlLabel
                    control={<Checkbox checked={wheelchair} onChange={e => setWheelchair(e.target.checked)} />}
                    label="Обслуживание инвалидов"
                  />
                  <FormControlLabel
                    control={<Checkbox checked={blind} onChange={e => setBlind(e.target.checked)} />}
                    label="Обслуживание незрячих клиентов"
                  />
                  <FormControlLabel
                    control={<Checkbox checked={nfc} onChange={e => setNfc(e.target.checked)} />}
                    label="NFC для банковских карт"
                  />
                  <FormControlLabel
                    control={<Checkbox checked={qrRead} onChange={e => setQrRead(e.target.checked)} />}
                    label="Чтение QR-кодов"
                  />
                  <FormControlLabel
                    control={<Checkbox checked={usd} onChange={e => setUsd(e.target.checked)} />}
                    label="USD"
                  />
                  <FormControlLabel
                    control={<Checkbox checked={chargeRub} onChange={e => setChargeRub(e.target.checked)} />}
                    label="Обмен RUB"
                  />
                  <FormControlLabel
                    control={<Checkbox checked={eur} onChange={e => setEur(e.target.checked)} />}
                    label="EUR"
                  />
                  <FormControlLabel
                    control={<Checkbox checked={rub} onChange={e => setRub(e.target.checked)} />}
                    label="RUB"
                  />
                </FormGroup>
                <Button variant="contained" sx={{ marginTop: 1, textAlign: 'center' }} onClick={() => getAtms()}>
                  Применить фильтры
                </Button>
              </Box>
              <Box component="div" sx={{ display: activeTab === 1 ? 'block' : 'none' }}>
                Офисы
              </Box>
            </>
          }
        </div>
      </Grid>
      <Grid item sx={{ flexBasis: '100%', overflow: 'hidden' }}>
        <div id="root"></div>
      </Grid>
    </Grid>
  );
};
