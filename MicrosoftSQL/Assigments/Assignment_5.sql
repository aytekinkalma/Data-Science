CREATE FUNCTION dbo.Factorial ( @iNumber int )
RETURNS INT
AS
BEGIN
DECLARE @i  int

    IF @iNumber <= 1
        SET @i = 1
    ELSE
        SET @i = @iNumber * dbo.Factorial( @iNumber - 1 )
RETURN (@i)
END

SELECT dbo.Factorial ( 10 )