# QR generator build

The site serves a local QR encoder bundle; no hosted QR service is used.

Run `npm ci`, `npm test`, and `npm run build` in this directory to reproduce the bundle. Keep website/qr-vendor.LICENSE.txt with the deployed script. The test decodes QR rasters at all offered image sizes using the independent jsQR decoder.
