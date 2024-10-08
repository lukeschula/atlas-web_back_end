-- SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.
DELIMITER //
CREATE TRIGGER email_validation_reset
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF OLD.email <> NEW.email
  THEN SET NEW.valid_email = FALSE;
  END IF;
END;
DELIMITER;