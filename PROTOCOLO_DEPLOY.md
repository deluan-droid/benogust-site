# Protocolo de Deploy — Site Benovet

**Leia este arquivo ANTES de fazer qualquer commit/push neste diretório.**

## Identidade deste site
- Site: **BenoVet** (Ciência, Saúde, Resultados — produtos veterinários)
- Domínio de produção: **https://benovet.com.br**

## Remote Git (GitHub)
- Repositório: `https://github.com/deluan-droid/benovet-site.git`
- ⚠️ **Atenção:** o GitHub redireciona este repositório — ele foi renomeado e o
  `git push` mostra a mensagem `This repository moved. Please use the new
  location: benogust-site.git`. O push ainda funciona e vai para o lugar certo,
  mas o nome real do repo no GitHub hoje é **`benogust-site`**, mesmo contendo
  o código do **Benovet**. Isso é confuso e é a causa raiz de um incidente
  anterior (ver PROTOCOLO_DEPLOY.md do site BenoGust).
- Branch de produção: `main`

## Projeto Vercel
- Nome do projeto: `benovet`
- Project ID: `prj_SctnH8NcfslWPiHj7pi2hEHn1vsq`
- Org/Team: `beno-vet` (`team_hpkUDfczzjt4usdLm555LI0e`)
- Domínio de produção vinculado: `benovet.com.br`

## ⚠️ Incidente conhecido (histórico — RESOLVIDO em 2026-09-13)
O repositório GitHub que hospeda o código deste site (`benogust-site`, apesar do
nome) já foi confundido/misturado com o código do site BenoGust mais de uma vez.
O projeto Vercel `benogust-site` (que serve `benogust.com.br`) chegou a estar
conectado a este mesmo repositório por engano, fazendo `benogust.com.br` servir
o conteúdo do Benovet.

**Correção aplicada:** o projeto Vercel `benogust-site` foi reconectado para o
repositório correto do BenoGust (`benogust-app`). Este site (Benovet) não foi
afetado na correção.

## Checklist obrigatório antes de commit/push/deploy
1. Confirme que está na pasta `Site Benovet` (não `Site BenoGust`).
2. Rode `git remote -v` — vai mostrar `benovet-site.git`, e o push pode exibir
   o aviso de "repository moved" para `benogust-site.git`. Isso é esperado
   neste repo específico, NÃO tente "corrigir" trocando a URL do remote.
3. Rode `vercel project inspect` (dentro desta pasta) e confirme `Name: benovet`.
4. Após o deploy, valide com `curl -sL https://benovet.com.br | grep '<title>'`
   — deve conter **"BenoVet"**, nunca "BenoGust".
5. Nunca rode `vercel git connect` neste projeto apontando para outro repo sem
   antes confirmar com o usuário — o projeto Vercel `benovet` deve continuar
   ligado ao repositório do Benovet.

## Dados oficiais da empresa (para rodapé/verificação Meta/Facebook)
- Razão Social: BENOGUST SOLUCOES AGRO LTDA
- CNPJ: 68.932.330/0001-59
