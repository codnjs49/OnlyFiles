CREATE TRIGGER client_delete
	BEFORE DELETE ON client
	FOR EACH ROW
	EXECUTE PROCEDURE client_delete();