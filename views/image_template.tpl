<html>
  <body>
    <h1>数字よみとり</h1>
    <form method="post" action="/start" enctype="multipart/form-data">
      手書きの0~9の数字の画像を入れてください: <input type="file" name="input_image"><br>
      <input type="submit" value="送信">
    </form>
    <ul>
      <li>pybotからの応答メッセージ: {{!output_text}}</li>
    </ul>
  </body>
</html>
