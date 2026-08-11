<!DOCTYPE html>
<html>
<head>
    <title>Saudação</title>
</head>
<body>
<h1>Saudações</h1>
    <h2>
        Olá, <%= request.getParameter("nome") %>! 
        Enviaremos novidades para <%= request.getParameter("email") %>.
    </h2>
</body>
</html>
