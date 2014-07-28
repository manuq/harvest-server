INSERT INTO gnome_alias VALUES ('gcalctool', 'Calculadora') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('Firefox', 'Firefox') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('Diccionario', 'Diccionario') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('gedit', 'Editor de textos gedit') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('Visor de libros electrónicos', 'Visor de libros electrónicos') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('gthumb', 'Visor de imágenes gThumb') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('Programa de manipulación de imágenes de GNU', 'Editor de imágenes GIMP') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('Tux Paint', 'Tux Paint') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('GeoGebra', 'GeoGebra') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('Terminal', 'Terminal') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('calibre', 'calibre') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('Audacity', 'Audacity') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('OpenOffice.org 3.3', 'OpenOffice') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('LibreOffice 3.6', 'LibreOffice') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('/usr/share/etoys/etoys.image', 'Etoys') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('inkscape', 'Editor de gráficos Inkscape') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('Web', 'Navegador Epiphany') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('npviewer.bin', 'Flash Player') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);
INSERT INTO gnome_alias VALUES ('plugin-container', 'Plugin de Firefox') ON DUPLICATE KEY UPDATE app_name = VALUES(app_name);


INSERT INTO activities VALUES ('uy.ceibal.GetBooksCeibalActivity', 'Biblioteca Ceibal') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.WebActivity', 'Navegar') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.RecordActivity', 'Grabar') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.JournalActivity', 'Diario') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.Calculate', 'Calculadora') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('com.ywwg.CartoonBuilderActivity', 'Creador de Historietas') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.CeibalNotifica', 'Ceibal Notifica') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.Chat', 'Charlar') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('tv.alterna.Clock', 'Clock') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.community.Colors', 'Colores') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.AcousticMeasure', 'Distancia') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.community.EnglishForFun', 'EnglishForFun') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.vpri.EtoysActivity', 'Etoys') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.worldwideworkshop.olpc.FlipSticks', 'Palillos') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.eq.FotoToon', 'FotoToon') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.ImageViewerActivity', 'Visor de imágenes') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('com.jotaro.ImplodeActivity', 'Implosionar') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.sugar.Jukebox', 'Máquina de discos') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.gnome.Labyrinth', 'Mapas mentales') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.Log', 'Log') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.Memorize', 'Memorizar') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.MeasureActivity', 'Medir') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('vu.lux.olpc.Maze', 'Laberinto') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.Oficina', 'Pintar') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.Pippy', 'Peppy') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.worldwideworkshop.PollBuilder', 'Encuesta') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.sugarlabs.PortfolioActivity', 'Obras') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.AbiWordActivity', 'Escribir') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.TamTamEdit', 'TamTamEdit') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.TamTamMini', 'TamTamMini') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.laptop.Terminal', 'Terminal') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('vu.lux.olpc.Speak', 'Hablar') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('org.tuxpaint', 'Tux Paint') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
INSERT INTO activities VALUES ('uy.edu.fing.geirea.conozcouruguay', 'Conozco Uruguay') ON DUPLICATE KEY UPDATE bundle_id = VALUES(bundle_id);
