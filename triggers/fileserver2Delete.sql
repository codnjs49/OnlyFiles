-- FUNCTION: public.fileserver1_delete()

-- DROP FUNCTION IF EXISTS public.fileserver1_delete();

CREATE OR REPLACE FUNCTION public.fileserver2_delete()
    RETURNS trigger
    LANGUAGE 'plpgsql'
AS $BODY$
BEGIN 
	-- DELETE from fileparts
	DELETE FROM server2
	WHERE file_id = NEW.file_id;
	Return OLD;
END;
$BODY$;
