select (sum(registrados)*100)/sum(universo) as porcentaje, sum(registrados) as registrados, sum(universo) as universo from muestras;
