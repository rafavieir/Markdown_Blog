date: 15-09-23
title: contato
category: .init




# Formulário de Contato

Para entrar em contato conosco, preencha o formulário abaixo:

<form action="/enviar" method="post">
  <label for="nome">Nome:</label>
  <input type="text" id="nome" name="nome" required><br><br>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required><br><br>

  <label for="mensagem">Mensagem:</label><br>
  <textarea id="mensagem" name="mensagem" rows="4" required></textarea><br><br>

  <input type="submit" value="Enviar">
</form>
