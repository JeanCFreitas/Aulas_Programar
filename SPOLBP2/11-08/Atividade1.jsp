<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Carrinho de Compras</title>
</head>
<body>
    <h2>Meu Carrinho de Compras</h2>
    <table>
        <tr>
            <th>Produto</th>
            <th>Preço (R$)</th>
        </tr>
        <%
            // Declaração do array de produtos (Nome e Preço)
            String[][] produtos = {
                {"Camiseta", "49.90"},
                {"Calça Jeans", "119.50"},
                {"Tênis", "199.99"},
                {"Boné", "29.90"}
            };

            double total = 0.0;

            // Loop for usando o objeto out para gerar o HTML
            for (int i = 0; i < produtos.length; i++) {
                String nome = produtos[i][0];
                double preco = Double.parseDouble(produtos[i][1]);
                total += preco;

                out.println("<tr>");
                out.println("<td>" + nome + "</td>");
                out.println("<td>R$ " + String.format("%.2f", preco) + "</td>");
                out.println("</tr>");
            }
        %>
        <tr>
            <th>Total do Carrinho</th>
            <th>R$ <% out.println(String.format("%.2f", total)); %></th>
        </tr>
    </table>
</body>
</html>