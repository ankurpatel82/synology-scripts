echo "Updating New LetsEncrypt Certificate"
cd /usr/syno/etc/certificate/_archive/Kpe0nP
openssl pkcs12 -export -inkey privkey.pem -in fullchain.pem -out fullchain.p12 -name unifi -password pass:unifi 
rm -f /volume1/docker/unifi/keystore
keytool -importkeystore -deststorepass aircontrolenterprise -destkeypass aircontrolenterprise -destkeystore /volume1/docker/unifi/keystore -srckeystore fullchain.p12 -srcstoretype PKCS12 -alias unifi -srcstorepass "unifi"
rm -f fullchain.p12
echo "Restart UniFi Controller"
docker restart unifi-controller