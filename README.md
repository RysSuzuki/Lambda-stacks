# AWS Lambda リポジトリ


### コマンド集


1. ビルド

   ```
   sam build
   ```

2. テスト
   ```
   sam local invoke <service名> --event events/event.json
   ```
3. デプロイ
   ```
   sam deploy --parameter-overrides $(../env.sh)
   ```