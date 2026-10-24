<!-- Korean draft translated from upstream/main README.md at cae7c375; cross-checked against README_ZH.md at the same commit. -->

<div align="center">

# CC Switch

### Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build, OpenCode, OpenClaw, Hermes Agent, Pi, MiniMax Code, Kimi Code, Oh My Pi를 위한 통합 관리 도구

**API 공급자를 클릭 한 번으로 전환하고 MCP, Skills, 프롬프트를 한곳에서 관리하세요. JSON / TOML / YAML 설정 파일을 직접 편집할 필요가 없습니다.**

[![Version](https://img.shields.io/github/v/release/farion1231/cc-switch?color=blue&label=version)](https://github.com/farion1231/cc-switch/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/farion1231/cc-switch/releases)
[![Built with Tauri](https://img.shields.io/badge/built%20with-Tauri%202-orange.svg)](https://tauri.app/)
[![Downloads](https://img.shields.io/github/downloads/farion1231/cc-switch/total)](https://github.com/farion1231/cc-switch/releases/latest)

<a href="https://trendshift.io/repositories/15372" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15372" alt="farion1231%2Fcc-switch | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<a href="https://www.star-history.com/#farion1231/cc-switch&Date"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=farion1231/cc-switch&theme=dark" /><img alt="Star History Rank" src="https://api.star-history.com/badge?repo=farion1231/cc-switch" width="196" height="55" /></picture></a>

### 🌐 유일한 공식 웹사이트: **[ccswitch.io](https://ccswitch.io)**

[English](README.md) | [中文](README_ZH.md) | [日本語](README_JA.md) | [Deutsch](README_DE.md) | 한국어 | [변경 이력](CHANGELOG.md)

**[다운로드](#download--installation) · [빠른 시작](#quick-start) · [주요 기능](#features) · [자주 묻는 질문](#faq) · [사용자 매뉴얼 (영문)](docs/user-manual/en/README.md)**

</div>

> 이 문서는 커뮤니티에서 관리하는 한국어 번역입니다. 사용자 매뉴얼과 일부 가이드는 영어 또는 중국어 문서로 연결됩니다.

## ❤️ 후원

> [후원사로 참여하고 싶으신가요?](mailto:support@ccswitch.io)

<details open>
<summary>클릭하여 접기</summary>

[![Kimi K2.7 Code](https://gcdn.moonshot.cn/growth-cdn/sponsor/kimi-en.png)](https://platform.kimi.ai?track_id=track-674ed6e2af924a5682a87421f7cf753a&aff=cc-switch)

Kimi K3는 Moonshot AI의 가장 강력한 모델이자 세계 최초의 오픈 소스 3T급 모델입니다. 2.8조 개의 매개변수, 네이티브 시각 기능, 100만 토큰 컨텍스트 창을 갖추고 장기 코딩 작업, 지식 업무, 추론에서 최고 수준의 성능을 제공합니다. CC Switch를 사용하면 여러 에이전트 도구에서 Kimi를 간편하게 설정하고 전환할 수 있습니다.

**Kimi Code 요금제** ([중국 사이트](https://www.kimi.com/code?aff=cc-switch) | [글로벌 사이트](https://www.kimi.ai/code?aff=cc-switch))를 이용하거나, Kimi Open Platform의 **API** ([중국 사이트](https://platform.kimi.com?track_id=track-7cf2b91dcde043eda6ef9a95951a042c&aff=cc-switch) | [글로벌 사이트](https://platform.kimi.ai?track_id=track-674ed6e2af924a5682a87421f7cf753a&aff=cc-switch))를 사용해 보세요.

**신규 사용자 충전 보너스**: 위 API 링크로 가입하고 첫 충전을 완료하면 충전 금액의 10%를 추가 API 크레딧으로 받습니다. 최대 CNY ¥1,000까지 지급됩니다.

---

<table>
<tr>
<td width="180"><a href="https://www.packyapi.ai/register?aff=cc-switch"><img src="assets/partners/logos/packycode.png" alt="PackyCode" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 PackyCode에 감사드립니다! PackyCode는 Claude Code, Codex, Gemini 등을 위한 안정적이고 효율적인 API 중계 서비스를 제공합니다. CC Switch 사용자를 위한 특별 할인도 준비되어 있습니다. <a href="https://www.packyapi.ai/register?aff=cc-switch">이 링크</a>로 가입하고 첫 충전 시 프로모션 코드 "cc-switch"를 입력하면 10% 할인받을 수 있습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://apinebula.ai/VjM74M"><img src="assets/partners/logos/apinebula_banner.png" alt="APINebula" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 APINEBULA에 감사드립니다! APINEBULA는 Galaxy Video Bureau 산하의 기업용 AI 통합 플랫폼으로, 풍부한 플랫폼 자원을 바탕으로 개발자, 팀, 기업에 안정적이고 경제적인 대규모 언어 모델 API를 제공합니다. Claude, GPT, Gemini 등 주요 모델의 모든 기능을 하나의 API로 이용할 수 있으며, 요금은 정가의 최저 10%부터 시작합니다. AI 코딩, 에이전트 개발, 업무 시스템 연동을 위해 설계되었으며 기업용 대규모 동시 요청, 정식 계약, 법인 계좌 이체, 청구서 발급을 지원합니다. <a href="https://apinebula.ai/VjM74M">이 링크</a>로 가입하고 첫 충전 시 프로모션 코드 <strong>"ccswitch"</strong>를 입력하면 <strong>10% 할인</strong>받을 수 있습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://www.aicodemirror.ai/register?invitecode=9915W3"><img src="assets/partners/logos/aicodemirror.jpg" alt="AICodeMirror" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 AICodeMirror에 감사드립니다! AICodeMirror는 Claude Code / Codex / Gemini CLI의 공식 채널을 통한 안정적인 중계 서비스와 기업용 동시 요청 처리, 신속한 청구서 발급, 연중무휴 전담 기술 지원을 제공합니다. Claude Code / Codex / Gemini 공식 채널을 각각 정가의 38% / 2% / 9%에 이용할 수 있으며 충전 시 추가 할인도 제공됩니다. CC Switch 사용자는 <a href="https://www.aicodemirror.ai/register?invitecode=9915W3">이 링크</a>로 가입하면 첫 충전 시 20% 할인받고, 기업 고객은 최대 25% 할인받을 수 있습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://pateway.ai/?ch=etzpm8&aff=WB6M6F67#/"><img src="assets/partners/logos/pateway.png" alt="PatewayAI" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 PatewayAI에 감사드립니다! PatewayAI는 AI를 집중적으로 사용하는 개발자를 위한 API 중계 서비스로, 공식 고품질 모델 API를 직접 중계하는 데 주력합니다. Claude 전체 제품군과 Codex 시리즈를 제공하며 100% 공식 채널을 사용합니다. 성능을 낮추거나 모델을 바꾸지 않으며 검증을 환영합니다. 투명하게 과금하고 토큰 단위 청구 내역을 항목별로 확인할 수 있습니다. 기업용 동시 요청 처리와 전용 관리 플랫폼도 제공하며 정식 계약과 청구서 발급을 지원합니다. 연락처는 공식 웹사이트를 확인하세요. 지금 <a href="https://pateway.ai/?ch=etzpm8&aff=WB6M6F67#/">이 링크</a>로 가입하면 $3 체험 크레딧을 받을 수 있습니다. 충전 가격은 정가의 최저 60%이며, 양방향 추천 보상은 최대 $150입니다!</td>
</tr>

<tr>
<td width="180"><a href="https://hao.ai/invite/DTBZS3OR"><img src="assets/partners/logos/haoai-banner.png" alt="hao.ai" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 hao.ai에 감사드립니다! hao.ai는 개발자와 팀을 위한 빠르고 안정적인 통합 LLM API 게이트웨이입니다. 하나의 API 키와 통합 인터페이스로 GPT, Claude, xAI Grok 등 주요 모델을 사용하며 OpenAI, Anthropic 등 일반적인 프로토콜과 SDK를 지원합니다. 모델 라우팅, 장애 조치, 팀 관리, 전체 요청 로그를 제공하고 모델 요금은 공식 기준가의 최저 15%로, AI 앱을 더 간단하고 안정적이며 경제적으로 구축할 수 있습니다. CC Switch 사용자는 <a href="https://hao.ai/invite/DTBZS3OR">이 링크</a>로 가입하면 첫 주문에 5% 추가 크레딧을 받습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://api.fenno.ai/register?redirect=/purchase?tab=subscription%26group=16&aff=P9MR3D3PLCNL"><img src="assets/partners/logos/fenno-banner.png" alt="Fenno.ai" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 Fenno.ai에 감사드립니다! Fenno.ai는 현재 Codex 중계에 주력하는 안정적이고 효율적인 API 중계 서비스입니다. OpenAI 및 Anthropic 프로토콜과 호환되며 Codex, Claude Code, OpenCode 등 주요 코딩 도구에서 유연하게 사용할 수 있습니다. 하루 수천억 토큰 규모의 기업 워크로드를 안정적으로 처리하고, 중국 내외 법인을 위한 B2B 정산과 청구서 발급을 지원합니다. CC Switch 사용자는 <a href="https://api.fenno.ai/register?redirect=/purchase?tab=subscription%26group=16&aff=P9MR3D3PLCNL">이 링크</a>에서 $1.99 체험 요금제를 구독하면 $50 상당의 크레딧(7일 유효)을 받을 수 있습니다. 추천 보상은 최대 20%이며 더 많이 초대할수록 더 많이 받을 수 있습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://runapi.host/register?aff=iOKB"><img src="assets/partners/logos/runapi.jpg" alt="RunAPI" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 RunAPI에 감사드립니다! RunAPI는 고성능의 안정적인 AI 모델 API 게이트웨이입니다. 하나의 API 키로 OpenAI, Claude, Gemini, DeepSeek, Grok 등 150개 이상의 주요 모델을 정가의 최저 10%에 이용할 수 있으며 높은 안정성을 제공합니다. Claude Code, OpenClaw 등과 원활하게 연동됩니다. CC Switch 사용자는 <a href="https://runapi.host/register?aff=iOKB">이 링크</a>로 가입하면 첫 충전 시 10% 할인받을 수 있습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://www.openmodel.ai?ref=cc-switch"><img src="assets/partners/logos/openmodel-banner.jpg" alt="OpenModel" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 OpenModel에 감사드립니다! OpenModel은 지원 모델을 Codex에서 최대 90%, Claude Code에서 최대 60% 할인해 제공하므로 기존 작업 방식을 유지하면서 API 비용을 줄일 수 있습니다. OpenModel API 키만 연결하면 평소처럼 Codex나 Claude Code를 사용할 수 있습니다. 지원 클라이언트를 자동으로 감지해 별도 매개변수나 수동 라우팅 설정 없이 할인 경로를 적용합니다. API 키마다 할인 경로를 일시적으로 사용할 수 없을 때 일반 요금으로 계속할지 중단할지도 설정할 수 있습니다. CC Switch 사용자는 <a href="https://www.openmodel.ai?ref=cc-switch">이 링크</a>로 가입하고 프로모션 코드 <strong>"cc-switch"</strong>를 사용하면 첫 충전 시 10% 할인받을 수 있습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://grooroute.pro/sign-up?aff=qqm9"><img src="assets/partners/logos/grooroute-banner.jpg" alt="GrooRoute Pro" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 GrooRoute Pro에 감사드립니다! GrooRoute Pro는 OpenAI, Claude, DeepSeek 등 주요 모델을 제공하는 안정적이고 원활한 AI API 중계 플랫폼입니다. 해외 서버에서 운영되며 요금 배율 등급을 직접 선택할 수 있습니다. 사용량 기반 과금과 구독 요금제를 모두 제공하고, 안정적인 경로와 빠른 응답으로 다양한 AI 기능을 편리하게 사용할 수 있습니다. CC Switch 사용자는 <a href="https://grooroute.pro/sign-up?aff=qqm9">이 링크</a>로 가입하면 무료 체험 크레딧 ¥5를 받습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://dit.ai?utm_source=ccswitch"><img src="assets/partners/logos/dit-banner.png" alt="DIT.ai" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 DIT.ai에 감사드립니다! DIT.ai는 여러 공급자의 모델을 저렴하게 라우팅하는 AI 토큰 거래 플랫폼이자 마켓플레이스입니다. 하나의 OpenAI 호환 API로 GPT, Claude, Gemini, DeepSeek, Grok, Llama 등 텍스트·이미지·영상·음성 분야의 주요 AI 모델 50개 이상을 제공합니다. 검증된 공급자들이 160개 이상의 경로에서 요청별로 경쟁하며, DIT가 가격과 품질을 실시간으로 비교해 최적의 경로를 선택합니다. 일반적으로 공식 정가보다 30–70% 저렴합니다. 에이전트나 AI 제품을 대규모로 운영하는 개발자, 스타트업, 팀을 위해 설계되었으며 Base URL과 API 키만 바꾸면 기존 기술 스택에서 자동 라우팅과 장애 조치를 사용할 수 있습니다. CC Switch 사용자는 <a href="https://dit.ai?utm_source=ccswitch">이 링크</a>로 가입하고 프로모션 코드 <strong>ccswitch</strong>를 사용하면 $5 가입 쿠폰을 받습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://buytoken.work/sign-up?aff=cc-switch"><img src="assets/partners/logos/buytoken-banner.png" alt="BuyToken" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 BuyToken에 감사드립니다! BuyToken은 Claude Code, Codex, DeepSeek 등의 중계 서비스를 제공하며, 기업용 동시 요청 처리와 신속한 청구서 발급을 지원하는 안정적인 장기 운영 서비스입니다. CC Switch 사용자는 <a href="https://buytoken.work/sign-up?aff=cc-switch">이 링크</a>로 가입하면 ¥3 체험 크레딧과 첫 충전 10% 할인 혜택을 받습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://gpt.ge/signup?aff=URNP"><img src="assets/partners/logos/vapi-banner.jpg" alt="V-API" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 V-API에 감사드립니다! V-API는 3년간 운영해 온 브랜드로, 개인, 개발자, 기업에 안정적이고 빠르며 안전한 고품질 LLM API 서비스를 제공합니다. 정식 계약과 중국의 일반·전용 부가가치세 청구서 발급도 지원합니다. CC Switch 사용자는 <a href="https://gpt.ge/signup?aff=URNP">이 링크</a>로 가입하면 첫 주문에서 ¥2 할인과 10% 할인을 함께 받을 수 있습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://agentmarket.fluxapay.xyz/marketplace/tokenplans"><img src="assets/partners/logos/fluxa-banner.png" alt="FluxA TokenPlan" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 FluxA와 Baidu AI Cloud에 감사드립니다! 두 회사가 공동 출시한 AgenticPlan은 AI 에이전트가 모델, API, 도구를 직접 구매·관리·사용하도록 지원합니다. DeepSeek V4, GLM 5.2, Kimi 등 대표 모델을 이용할 수 있는 Baidu Qianfan TokenPlan을 최대 40% 할인해 제공하며, 검색, 데이터 수집, 소셜 미디어, 금융, 암호화폐, 이미지·영상 생성 등 13,000개 이상의 유료 API에 사용할 수 있는 FluxA AgentMarket API 크레딧도 추가로 제공합니다.<br>사용자가 승인하면 에이전트가 공식 Visa 카드로 자원을 구매하고, API 키를 관리하며, 사용량과 요금제 갱신을 확인할 수도 있습니다. 작업의 자율 수행을 넘어 예산 계획까지 직접 수행하도록 돕습니다. <a href="https://agentmarket.fluxapay.xyz/marketplace/tokenplans">이 링크</a>에서 구매하세요!</td>
</tr>

<tr>
<td width="180"><a href="https://aigocode.net/invite/CC-SWITCH"><img src="assets/partners/logos/aigocode.png" alt="AIGoCode" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 AIGoCode에 감사드립니다! AIGoCode는 Claude Code, Codex, 최신 Gemini 모델을 통합해 안정적이고 효율적이며 경제적인 AI 코딩 서비스를 제공합니다. 유연한 구독 요금제, 계정 정지 위험 없는 이용, 중국 내에서 VPN이 필요 없는 직접 접속, 빠른 응답을 제공합니다. CC Switch 사용자는 <a href="https://aigocode.net/invite/CC-SWITCH">이 링크</a>로 가입하면 첫 충전 금액의 10%를 추가 크레딧으로 받습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://aicoding.inc/i/CCSWITCH"><img src="assets/partners/logos/aicoding.jpg" alt="AICoding" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 AICoding에 감사드립니다! AICoding은 저렴한 가격의 글로벌 AI 모델 API 중계 서비스입니다. Claude Code는 정가의 19%, GPT는 1%에 이용할 수 있습니다. 수백 개 기업이 사용하는 경제적인 AI 서비스로, Claude Code, GPT, Gemini 및 주요 중국 모델을 지원합니다. 기업용 대규모 동시 요청, 신속한 청구서 발급, 연중무휴 전담 기술 지원도 제공합니다. CC Switch 사용자는 <a href="https://aicoding.inc/i/CCSWITCH">이 링크</a>로 가입하면 첫 충전 시 10% 할인받을 수 있습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://subrouter.ai/register?aff=l3ri"><img src="assets/partners/logos/subrouter-banner.png" alt="SubRouter" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 SubRouter에 감사드립니다! SubRouter는 AI 서비스 운영자를 위한 마켓플레이스이자 스마트 라우팅 플랫폼입니다. 판매자는 운영 사이트 개설, 상품 출시, 사용자·모델·요금 관리를 할 수 있고, 사용자는 서비스를 찾아 하나의 통합 API로 안정적인 AI 모델을 이용할 수 있습니다. <a href="https://subrouter.ai/register?aff=l3ri">이 링크</a>에서 가입하세요!</td>
</tr>

<tr>
<td width="180"><a href="https://www.shengsuanyun.com/?from=CH_4HHXMRYF"><img src="assets/partners/logos/shengsuanyun.png" alt="Shengsuanyun" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 Shengsuanyun에 감사드립니다! Shengsuanyun은 AI 네이티브 팀을 위한 산업용 AI 작업 병렬 실행 플랫폼입니다. 모델 마켓플레이스에서 Claude, ChatGPT, Gemini 등 중국 내외 LLM과 멀티미디어 모델을 직접 공급합니다. 역공학이나 성능 저하 없이 플랫폼 전체 SLA 가용률 99.7%를 제공하며, <a href="https://watch.shengsuanyun.com/status/shengsuanyun">모니터링 대시보드</a>에서 모든 서비스의 정상 상태를 확인할 수 있습니다. 팀 비용과 권한의 세부 관리, 스마트 라우팅, 보안, BYOK(Bring Your Own Key) 호스팅을 위한 기업 맞춤형 게이트웨이도 제공합니다. 사용량 기반 과금과 토큰 요금제(출시 예정)를 제공하며 청구서 발급을 지원합니다. 신규 사용자는 <a href="https://www.shengsuanyun.com/?from=CH_4HHXMRYF">이 링크</a>로 가입하면 ¥10 크레딧과 첫 충전 10% 추가 크레딧을 받습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://88api.ai/sign-up?aff=HSGY"><img src="assets/partners/logos/88api-banner-en.jpg" alt="88API" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 88API Token Aggregation Platform에 감사드립니다! 88API는 홍콩 회사가 운영하는 통합 다중 모델 API 플랫폼으로, 개발자, 크리에이터, AI 앱 사용자를 위해 설계되었습니다. 하나의 인터페이스로 텍스트, 이미지, 음성, 영상 모델을 제공하며 AI 코딩, 번역, 콘텐츠 제작, 음성 더빙, 이미지·영상 생성 등의 작업을 지원합니다. CC Switch에서 공급자로 추가하고 바로 전환할 수 있습니다. 주요 국제 결제 수단, 청구서 발급, 기업용 안정적인 서비스를 지원합니다. <a href="https://88api.ai/sign-up?aff=HSGY">이 링크</a>로 가입하면 전용 추가 크레딧을 받습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://apikey.fan/register?aff=CCSwitch"><img src="assets/partners/logos/apikey_banner.png" alt="APIKEY.FUN" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 APIKEY.FUN에 감사드립니다! APIKEY.FUN은 기업과 개인 개발자에게 안정적이고 효율적이며 저렴한 AI 모델 API를 제공하는 기업용 AI 중계 플랫폼입니다. Claude, OpenAI, Gemini 등 주요 모델을 정가의 최저 7%에 이용할 수 있습니다. 이 프로젝트의 <a href="https://apikey.fan/register?aff=CCSwitch">전용 가입 링크</a>로 가입하면 <strong>충전 시 최대 5% 상시 할인</strong> 혜택을 받을 수 있습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://9527.codes/register?aff=e5zI"><img src="assets/partners/logos/9527-banner.png" alt="9527CODE" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 9527CODE에 감사드립니다! 9527 CODE는 안정성과 서비스 품질을 중시하는 기업용 AI 중계 플랫폼으로, Claude Code, Codex 등 주요 모델을 빠르고 안정적인 고품질 서비스로 제공합니다. 장기 안정성, 경로 품질, 지속적인 가용성을 바탕으로 기업과 AI 집중 사용자에게 효율적인 통합 모델 접근 환경을 제공합니다. 1년간 연속 운영, 99.9% 서비스 안정성, 연중무휴 상담원 기술 지원을 제공합니다. 이 프로젝트의 <a href="https://9527.codes/register?aff=e5zI">전용 가입 링크</a>로 가입한 신규 사용자는 고객 지원에 연락해 체험 크레딧을 받을 수 있으며, 추천 캐시백에는 한도가 없습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://teamorouter.cn/?utm_source=cc_switch&utm_medium=referral&utm_campaign=ai_directory"><img src="assets/partners/logos/TeamoRouter-banner.png" alt="TeamoRouter" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 TeamoRouter에 감사드립니다! TeamoRouter는 개발자, AI 팀, 기업을 위한 기업용 Agentic LLM 게이트웨이입니다. 구독 없이 하나의 통합 API로 Claude Code, Codex, Gemini CLI, OpenAI Codex 등 주요 AI 에이전트를 사용할 수 있으며 API 요금은 최대 90% 할인됩니다. 일반적인 중계 서비스와 달리 OpenAI, Anthropic, Vertex, Azure, AWS bedrock 등 수백 개 공식 모델 공급자와 신뢰할 수 있는 인프라 파트너를 통합합니다. 모든 공급자에 대해 에이전트 프로토콜 100% 호환성, 캐시 성능, 요청 추적 가능성을 검증해 역공학이나 성능을 낮춘 엔드포인트 대신 안정적인 품질을 제공합니다. 공식 서비스에 가까운 TTFT, 99.6% SLA, 최대 5,000 QPM 처리량, 높은 캐시 적중률로 장시간 에이전트 작업의 토큰 비용을 줄입니다. 통합 결제, 팀 관리, BYOK, 스마트 라우팅, 사용량 분석, 동적 공급자 최적화, 전담 지원도 제공합니다. Teamo Desktop에서는 API 키 관리나 수동 게이트웨이 설정 없이 Claude Code, Codex, Gemini CLI 등을 클릭 한 번으로 설정할 수 있습니다. <a href="https://teamorouter.cn/?utm_source=cc_switch&utm_medium=referral&utm_campaign=ai_directory">이 링크</a>로 가입한 신규 사용자는 첫 충전 시 10% 할인받을 수 있습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://ppio.com/activity/ccswitch"><img src="assets/partners/logos/ppio-banner.png" alt="PPIO" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 PPIO에 감사드립니다! PPIO는 PPTV 창립자 Yao Xin과 전 수석 아키텍트 Wang Wenyu가 2018년에 공동 설립한 중국의 주요 독립 Agentic Cloud 공급자입니다. 하나의 API 키로 DeepSeek-V4-Flash, Kimi-K3, GLM-5.2, MiniMax-M3 등 대표 오픈 소스 모델을 모두 사용할 수 있습니다. 기업용 Token Plan은 최대 40% 할인과 200석을 지원하며, Fusion 혼합 모델은 Fable5에 필적하는 성능을 10분의 1 가격에 제공합니다. <a href="https://ppio.com/activity/ccswitch">이 링크</a>로 가입하고 본인 인증을 완료하면 ¥10 크레딧 쿠폰을 받으며, 친구의 충전 금액에 대해 최대 15% 캐시백을 받을 수 있습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://www.newapi.ai/"><img src="assets/partners/logos/newapi-banner.png" alt="new-api" width="150"></a></td>
<td>오픈 소스 AI 인프라 프로젝트 <a href="https://www.newapi.ai/">new-api</a>의 든든한 지원에 감사드립니다! new-api는 QuantumNous의 오픈 소스 AI 인프라 프로젝트로, 활발한 개발과 폭넓은 도입을 바탕으로 LLM 통합 접근·배포 분야를 이끌고 있습니다. 개발자, 팀, 기업이 관리하기 쉽고 확장 가능한 AI 서비스 플랫폼을 더 낮은 비용으로 구축하도록 돕습니다. 오픈 소스 생태계에 뿌리를 둔 프로젝트로서 다른 우수한 오픈 소스 프로젝트의 지속적인 성장도 후원하고자 합니다. 🌟 new-api에 Star를 눌러 응원해 주세요: <a href="https://github.com/QuantumNous/new-api">https://github.com/QuantumNous/new-api</a>. 웹사이트: <a href="https://www.newapi.ai/">https://www.newapi.ai/</a>.</td>
</tr>

<tr>
<td width="180"><a href="https://claudecn.ai/register?aff=HEL9"><img src="assets/partners/logos/claudecn.jpg" alt="ClaudeCN" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 ClaudeCN에 감사드립니다! ClaudeCN은 등록 법인이 운영하는 기업용 AI 게이트웨이 플랫폼입니다. Claude, GPT, DeepSeek 등 주요 모델에 상용 고가용성 API를 제공하며, 법인 계좌 이체, 계약 체결, 규정 준수 등 정식 기업 구매 절차를 지원합니다. <a href="https://claudecn.ai/register?aff=HEL9">이 링크</a>에서 가입하세요!</td>
</tr>

<tr>
<td width="180"><a href="https://www.byteplus.com/en/product/modelark?utm_campaign=hw&utm_content=ccswitch&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=ccswitch"><img src="assets/partners/logos/byteplus.png" alt="BytePlus" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 Dola seed에 감사드립니다! Dola Seed 2.0은 ByteDance가 글로벌 시장을 위해 자체 개발한 전 모달리티 범용 대규모 모델입니다. 통합 멀티모달 아키텍처를 바탕으로 텍스트, 이미지, 음성, 영상의 통합 이해와 생성을 지원합니다. 에이전트 협업을 기본 지원하며 추론, 장기 작업 실행, 도구 연동, 코딩 능력을 갖추고 있습니다. 스마트 차량 실내 시스템, 개인 비서, 교육, 고객 지원, 마케팅, 소매 등 다양한 분야에 활용할 수 있습니다. 멀티모달 인식, 복잡한 작업의 전체 수행, 안정적인 상호작용, 데이터 보안에 강점이 있으며 ModelArk에서 쉽게 이용하고 배포할 수 있습니다. <a href="https://www.byteplus.com/en/product/modelark?utm_campaign=hw&utm_content=ccswitch&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=ccswitch">이 링크</a>로 가입하면 모델마다 무료 추론 할당량 500,000토큰을 받습니다. <a href="https://www.volcengine.com/activity/ai618?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=ccswitch">중국 본토 개발자는 여기를 클릭하세요</a></td>
</tr>

<tr>
<td width="180"><a href="https://cloud.siliconflow.cn/i/YflgU2Ve"><img src="assets/partners/logos/silicon_en.jpg" alt="SiliconFlow" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 SiliconFlow에 감사드립니다! SiliconFlow는 언어, 음성, 이미지, 영상 모델을 한곳에서 빠르고 안정적으로 제공하는 고성능 AI 인프라 및 모델 API 플랫폼입니다. 사용량 기반 과금, 다양한 멀티모달 모델, 고속 추론, 기업용 안정성을 통해 개발자와 팀이 AI 앱을 더 효율적으로 구축하고 확장하도록 돕습니다. <a href="https://cloud.siliconflow.cn/i/YflgU2Ve">이 링크</a>로 가입하고 실명 인증을 완료하면 플랫폼 모델 전반에 사용할 수 있는 ¥16 추가 크레딧을 받습니다. OpenClaw도 지원하므로 SiliconFlow API 키를 연결해 주요 AI 모델을 무료로 호출할 수 있습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://a6api.com/register?aff=AqNr"><img src="assets/partners/logos/a6-banner-en.jpg" alt="A6API" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 <a href="https://a6api.com/register?aff=AqNr">A6API</a>에 감사드립니다! A6API는 Claude, GPT, Gemini, Codex 등 주요 모델을 제공하는 통합 AI 모델 API 플랫폼입니다. 여러 공급자가 같은 모델을 경쟁력 있는 가격으로 제공할 수 있으며, 스마트 라우팅이 더 안정적이고 저렴한 경로를 자동 선택하고 장애 조치를 수행합니다. 요청 실패와 비용을 줄이고 안정성을 높일 수 있습니다. 개인 개발자, AI 제품 팀, 스튜디오 모두 다양한 형식을 지원하는 통합 인터페이스로 적은 이전 비용에 빠르게 연동할 수 있습니다. <a href="https://a6api.com/register?aff=AqNr">이 링크</a>로 가입한 신규 사용자에게 무료 체험 크레딧을 제공합니다. 먼저 체험한 뒤 저렴하게 사용해 보세요.</td>
</tr>

<tr>
<td width="180"><a href="https://www.compshare.cn/coding-plan?ytag=GPU_YY_YX_git_cc-switch"><img src="assets/partners/logos/ucloud.png" alt="Compshare" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 Compshare에 감사드립니다! Compshare는 UCloud의 AI 클라우드 플랫폼으로, 하나의 키로 중국 내외의 다양한 모델 API를 안정적으로 제공합니다. 경제적인 중국 모델의 월정액·사용량 기반 Coding Plan과 안정적인 공식 중계 해외 모델을 제공합니다. Claude Code, Codex, API 접근, 기업용 동시 요청 처리, 연중무휴 기술 지원, 셀프서비스 청구서 발급을 지원합니다. <a href="https://www.compshare.cn/coding-plan?ytag=GPU_YY_YX_git_cc-switch">이 링크</a>로 가입하면 무료 체험 크레딧 CNY 5를 받습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://www.ccsub.net/register?ref=Y6Z8DXEA"><img src="assets/partners/logos/ccsub.svg" alt="CCSub" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 CCSub에 감사드립니다! CCSub는 Claude.ai 구독을 바로 대체할 수 있는 안정적이고 경제적인 AI API 중계 플랫폼입니다. 하나의 API 키로 Claude Opus 4.8, Sonnet, Haiku, GPT-5, Gemini, DeepSeek를 직접 API 비용의 약 30%에 사용할 수 있으며 전 세계 어디서나 VPN 없이 이용할 수 있습니다. Claude Code, Codex, Cursor, Cline, Continue, Windsurf 등 주요 AI 코딩 도구와 호환됩니다. <a href="https://www.ccsub.net/register?ref=Y6Z8DXEA">이 링크</a>로 가입하면 무료 크레딧 $5를 받습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://sssaicodeapi.com/register?ref=DCP0SM"><img src="assets/partners/logos/sssaicode.png" alt="SSSAiCode" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 SSSAiCode에 감사드립니다! SSSAiCode는 안정적이고 저렴한 Claude 및 Codex 모델 서비스를 제공하는 신뢰할 수 있는 API 중계 서비스이며, 당일 신속한 청구서 발급을 지원합니다. CC Switch 사용자는 <a href="https://sssaicodeapi.com/register?ref=DCP0SM">이 링크</a>로 가입하면 충전할 때마다 추가 크레딧 $10를 받습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://soleapi.com/r/ccswitch"><img src="assets/partners/logos/soleapi-banner.png" alt="SoleAPI" width="150"></a></td>
<td>이 프로젝트를 지원해 주신 SoleAPI에 감사드립니다! SoleAPI는 개발자와 기업을 위한 AI 모델 게이트웨이로, 하나의 API 키로 Claude, GPT, Gemini 등 30개 이상의 주요 모델을 제공합니다. OpenAI 및 Anthropic 프로토콜과 기본 호환되므로 Claude Code, Codex, Cursor, 기존 SDK의 Base URL만 바꾸면 사용할 수 있습니다. 지연 시간과 업스트림 상태에 따라 실시간으로 라우팅하며, 밀리초 단위의 백업 경로 자동 장애 조치, 99.99% 서비스 가용성, 연중무휴 기술 지원을 제공합니다. 모든 호출은 하나의 청구서에 모이며 요청별 토큰과 비용 내역을 언제든 확인할 수 있습니다. 이 프로젝트의 <a href="https://soleapi.com/r/ccswitch">전용 가입 링크</a>로 가입하면 무료 체험 크레딧을 받고, 친구를 초대해 충전하면 지속적인 캐시백을 받을 수 있습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://www.micuapi.ai/register?aff=aOYQ"><img src="assets/partners/logos/mikubanner.svg" alt="Micu" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 Micu API에 감사드립니다! Micu API는 높은 안정성과 뛰어난 가격 대비 성능을 목표로 하는 글로벌 LLM 중계 서비스입니다. 등록 기업이 운영해 서비스 중단 위험 없이 이용할 수 있으며 공식 청구서를 신속하게 발급합니다. 부담 없는 체험을 위해 최소 충전 제한 없이 ¥1부터 충전하고 언제든 수수료 없이 환불받을 수 있습니다. CC Switch 사용자는 <a href="https://www.micuapi.ai/register?aff=aOYQ">이 링크</a>로 가입하고 충전 시 프로모션 코드 "ccswitch"를 입력하면 <strong>10% 할인</strong>받을 수 있습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://www.rightapi.ai/register?aff=CCSWITCH"><img src="assets/partners/logos/rightcode.jpg" alt="RightCode" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 Right Code에 감사드립니다! Right Code는 Claude Code, Codex, Gemini 등의 모델을 안정적으로 라우팅하며 사용량 기반 과금과 월 구독을 모두 제공합니다. 충전 시 청구서를 발급하며 기업과 팀 사용자에게 전담 일대일 지원을 제공합니다. CC Switch 사용자는 <a href="https://www.rightapi.ai/register?aff=CCSWITCH">이 링크</a>로 가입하면 충전할 때마다 결제 금액의 5%에 해당하는 사용량 기반 크레딧을 추가로 받습니다.</td>
</tr>

<tr>
<td width="180"><a href="https://cubence.com/signup?code=CCSWITCH&source=ccs"><img src="assets/partners/logos/cubence.png" alt="Cubence" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 Cubence에 감사드립니다! Cubence는 Claude Code, Codex, Gemini 등을 위한 안정적이고 효율적인 API 중계 서비스로, 사용량 기반 과금과 월 요금제 등 유연한 결제 방식을 제공합니다. CC Switch 사용자는 <a href="https://cubence.com/signup?code=CCSWITCH&source=ccs">이 링크</a>로 가입하고 충전 시 프로모션 코드 "CCSWITCH"를 입력하면 매 충전마다 10% 할인받을 수 있습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://crazyrouter.com/register?aff=OZcm&ref=cc-switch"><img src="assets/partners/logos/crazyrouter.png" alt="Crazyrouter" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 Crazyrouter에 감사드립니다! Crazyrouter는 하나의 API 키로 Claude Code, Codex, Gemini CLI 등을 포함한 300개 이상의 모델을 제공하는 고성능 AI API 통합 플랫폼입니다. 모든 모델을 공식 요금의 최저 55%에 이용할 수 있으며 자동 장애 조치, 스마트 라우팅, 무제한 동시 요청 처리를 지원합니다. CC Switch 사용자는 <a href="https://crazyrouter.com/register?aff=OZcm&ref=cc-switch">이 링크</a>로 가입하고 고객 지원에 연락하면 <strong>무료 크레딧 $2</strong>를 받습니다. 첫 충전 시 프로모션 코드 `CCSWITCH`를 입력하면 <strong>30% 추가 크레딧</strong>도 받습니다!</td>
</tr>

<tr>
<td width="180"><a href="https://www.dmxapi.cn/register?aff=bUHu"><img src="assets/partners/logos/dmx-en.jpg" alt="DMXAPI" width="150"></a></td>
<td>이 프로젝트를 후원해 주신 DMXAPI에 감사드립니다! DMXAPI는 200개 이상의 기업 고객에게 전 세계 대규모 모델 API를 제공하며 하나의 API 키로 모든 글로벌 모델을 사용할 수 있습니다. 즉시 청구서 발급, 무제한 동시 요청 처리, $0.15부터 시작하는 요금, 연중무휴 기술 지원을 제공합니다. GPT/Claude/Gemini는 모두 32% 할인, 중국 모델은 20–50% 할인, Claude Code 전용 모델은 66% 할인됩니다! <a href="https://www.dmxapi.cn/register?aff=bUHu">여기에서 가입하세요</a></td>
</tr>

</table>

</details>

## CC Switch를 사용하는 이유

Claude Code, Codex, Gemini CLI 같은 AI 코딩 도구는 저마다 설정 형식이 다릅니다. API 공급자를 전환하려면 JSON, TOML, YAML 또는 `.env` 파일을 직접 편집해야 하고, MCP, Skills, 프롬프트도 도구마다 따로 관리해야 합니다.

**CC Switch**는 이 모든 작업을 하나의 데스크톱 앱에 모았습니다. 프리셋을 선택하고 키를 입력하면 클릭 한 번으로 전환할 수 있습니다. 전환 시 엔드포인트, 키, 모델 등 연결 정보만 바꾸므로 직접 추가한 플러그인, Hooks, MCP, 주석은 그대로 유지됩니다.

- **하나의 앱으로 12개 도구 관리** — Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build, OpenCode, OpenClaw, Hermes, Pi, MiniMax Code, Kimi Code, Oh My Pi
- **설정 파일을 직접 편집할 필요 없음** — AWS Bedrock, NVIDIA NIM, 서드파티 API 중계 서비스를 포함한 90개 이상의 공급자 프리셋
- **직접 연결, 라우팅, 통합을 필요에 따라 선택** — 직접 연결은 도구가 공급자에 바로 연결합니다. 라우팅은 로컬 컴퓨터를 통해 요청을 전달하며 API 형식 변환과 자동 장애 조치를 지원하므로 Claude Code에서 GPT를, Codex에서 Claude를 사용할 수 있습니다. 통합은 여러 공급자의 모델을 Claude Code 또는 Codex의 모델 목록 하나에 모으며, 선택한 모델의 공급자로 요청을 보냅니다.
- **MCP, Skills, 프롬프트 통합 관리** — MCP 서버와 Skills를 한 번 추가한 뒤 동기화할 도구를 선택합니다. 프롬프트는 도구별로 관리합니다.
- **읽기 쉬운 세션 기록** — 각 도구의 세션 로그를 읽기 화면으로 변환해 각 턴에서 수행한 작업, 변경한 파일, 실패한 단계를 한눈에 보여 줍니다.
- **사용량과 할당량을 한눈에 확인** — 로컬 라우팅 없이도 토큰 사용량과 비용을 추적합니다. 남은 구독 할당량과 계정 잔액은 공급자 카드와 트레이에 바로 표시됩니다.
- **여러 운영체제 지원** — Tauri 2 기반의 Windows, macOS, Linux용 네이티브 데스크톱 앱

## 스크린샷

<table>
<tr>
<td align="center" width="50%"><img src="assets/release-notes/v4.0.0/main-en.png" alt="메인 화면: 사이드바, 직접 연결·라우팅·통합 탭, 공급자 카드" width="400"><br>메인 화면</td>
<td align="center" width="50%"><img src="assets/release-notes/v4.0.0/apps-en.png" alt="앱 페이지: AI 코딩 도구의 버전, 설치 및 업그레이드를 한곳에서 관리" width="400"><br>앱 페이지</td>
</tr>
<tr>
<td align="center"><img src="assets/release-notes/v4.0.0/agg-en.png" alt="통합 모드: 기본 공급자 하나와 여러 추가 공급자" width="400"><br>통합 모드</td>
<td align="center"><img src="assets/release-notes/v4.0.0/agg-codex-en.png" alt="여러 공급자의 모델을 표시하는 Codex 모델 선택기" width="400"><br>Codex의 통합 모델 목록</td>
</tr>
<tr>
<td align="center"><img src="assets/release-notes/v4.0.0/session-en.png" alt="세션 읽기 화면: 단계 요약, 도구 호출 세부 정보, 대화 개요" width="400"><br>세션 읽기 화면</td>
<td align="center"><img src="assets/release-notes/v4.0.0/usage-en.png" alt="사용 통계: 히트맵과 요청 로그" width="400"><br>사용 통계</td>
</tr>
</table>

<a id="download--installation"></a>

## 다운로드 및 설치

### 시스템 요구 사항

- **Windows**: Windows 10 이상
- **macOS**: macOS 12 (Monterey) 이상
- **Linux**: glibc 2.35+와 WebKitGTK 4.1을 제공하는 x86_64 또는 ARM64 환경. 예: Ubuntu 22.04+, Debian 12+, 최신 Fedora. RHEL / Rocky / Alma 8–9는 아직 지원하지 않습니다.

### Windows

[Releases](../../releases) 페이지에서 최신 `CC-Switch-v{version}-Windows.msi` 설치 파일 또는 `CC-Switch-v{version}-Windows-Portable.zip` 포터블 버전을 다운로드하세요. Windows on ARM에서는 `CC-Switch-v{version}-Windows-arm64.msi` 또는 `CC-Switch-v{version}-Windows-arm64-Portable.zip`을 다운로드하세요.

### macOS

**방법 1: Homebrew로 설치 (권장)**

```bash
brew install --cask cc-switch
```

업데이트:

```bash
brew upgrade --cask cc-switch
```

**방법 2: 직접 다운로드**

[Releases](../../releases) 페이지에서 `CC-Switch-v{version}-macOS.dmg` (권장) 또는 `.zip`을 다운로드하세요. Apple Silicon과 Intel Mac에서 모두 네이티브로 실행되는 Universal 빌드입니다.

> **참고**: macOS용 CC Switch는 코드 서명과 Apple 공증을 완료했습니다. 설치 후 바로 실행할 수 있습니다.

### Arch Linux

**paru로 설치 (권장)**

```bash
paru -S cc-switch-bin
```

### Linux

[Releases](../../releases) 페이지에서 최신 Linux 빌드를 다운로드하세요.

- `CC-Switch-v{version}-Linux-x86_64.deb` / `-Linux-arm64.deb` (Debian/Ubuntu)
- `CC-Switch-v{version}-Linux-x86_64.rpm` / `-Linux-arm64.rpm` (WebKitGTK 4.1을 제공하는 Fedora 및 기타 RPM 배포판)
- `CC-Switch-v{version}-Linux-x86_64.AppImage` / `-Linux-arm64.AppImage` (위 시스템 요구 사항을 충족하는 배포판)

> **Flatpak**: 공식 릴리스에는 포함되지 않습니다. `.deb`를 사용해 직접 빌드할 수 있습니다. 방법은 [`flatpak/README.md`](flatpak/README.md)를 참고하세요.

<a id="quick-start"></a>

## 빠른 시작

### 기본 사용법

1. **공급자 추가**: 사이드바에서 관리할 도구를 선택한 뒤 페이지 오른쪽 상단의 "+" (공급자 추가)를 클릭하고 프리셋을 선택하거나 사용자 정의 설정을 만듭니다.
2. **공급자 전환**:
   - 메인 화면: 공급자를 선택한 뒤 "활성화"를 클릭합니다. OpenCode, OpenClaw, Hermes, MiniMax Code, Kimi Code의 버튼은 "추가", Pi와 Oh My Pi의 버튼은 "활성화" / "제거"입니다. 이 7개 도구는 여러 공급자를 동시에 추가할 수 있는 공존 방식입니다.
   - 시스템 트레이: 도구마다 "이름 · 모드 · 공급자 · 할당량"이 한 줄로 표시됩니다. 하위 메뉴에서 공급자 이름을 클릭해 전환합니다. Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build를 지원합니다.
3. **변경 사항 적용**: Claude Code는 재시작할 필요가 없습니다. Codex, Gemini CLI, Grok Build는 터미널 또는 CLI 도구를 재시작해야 하며, Claude Desktop은 앱 자체를 재시작해야 합니다. 자세한 내용은 자주 묻는 질문을 참고하세요.
4. **공식 로그인으로 복귀**: 목록의 기본 제공 공식 공급자(예: "Claude Official")로 전환하고 도구를 재시작한 뒤 해당 도구의 로그인/OAuth 절차를 따릅니다.
5. **라우팅 및 통합 (선택 사항)**: Claude Code, Codex, Gemini CLI, Grok Build 페이지 상단에는 "직접 연결" / "라우팅" 탭이 있으며, Claude Code와 Codex에는 "통합"도 있습니다. 탭을 클릭하는 것만으로는 설정이 바뀌지 않습니다. 실제로 전환하려면 페이지에서 "라우팅 시작" 또는 "통합 모드로 전환"을 클릭하고, 돌아가려면 "직접 연결로 돌아가기"를 클릭하세요. 라우팅을 사용하면 Claude Code에서 OpenAI 또는 Gemini 형식의 공급자를, Codex에서 Claude를 사용할 수 있습니다. 통합을 사용하면 여러 공급자의 모델을 하나의 모델 목록에 모을 수 있습니다.
6. **도구 관리**: 사이드바의 "앱" 페이지에서 각 AI 코딩 도구의 버전, 설치 위치, 설치 출처를 한곳에서 확인할 수 있습니다. 설치, 업그레이드, 전체 업그레이드를 실행하고 사이드바에 표시할 도구를 선택할 수 있습니다.

### MCP, 프롬프트, Skills, 프로젝트, 세션

- **MCP**: 사이드바에서 "MCP"를 클릭하고 템플릿이나 사용자 정의 설정으로 서버를 추가하거나 "기존 설정 가져오기"를 선택한 뒤 도구별 동기화를 켭니다.
- **프롬프트**: 사이드바에서 "프롬프트"를 클릭하고 Markdown 편집기로 프롬프트를 만든 뒤 활성화하면 해당 도구의 프롬프트 파일에 저장됩니다.
- **Skills**: 사이드바에서 "Skills" → "Skills 살펴보기"를 클릭하고 skills.sh를 검색하거나 GitHub 저장소를 둘러본 뒤 지원 도구에 클릭 한 번으로 설치합니다.
- **프로젝트**: 먼저 "설정 → 일반"에서 "프로젝트 전환기 표시"를 켭니다. Claude Code, Claude Desktop 또는 Codex 페이지 상단의 프로젝트 전환기를 열고 "새 프로젝트"를 선택해 현재 설정을 저장하세요. 이후 전환기에서 프로젝트를 선택하면 전체 구성을 한 번에 전환할 수 있습니다.
- **세션**: 사이드바에서 "세션"을 클릭해 대화 기록을 찾아보고 검색하거나, 읽기 화면을 열거나, 각 도구의 세션을 복원합니다.
- **인증 센터**: 사이드바에서 "인증 센터"를 클릭해 GitHub Copilot, ChatGPT, xAI (Grok), Kimi Code 계정으로 로그인하고 구독을 공급자로 사용할 수 있습니다. Kimi Code는 여러 공식 계정을 지원하며, 각 계정에 별도의 자격 증명과 네이티브 공급자가 생성됩니다. 첫 로그인은 Kimi의 네이티브 기본 자격 증명 슬롯을 사용합니다. 여기서 로그인, 재인증, 로그아웃을 관리합니다. 네이티브 설정에 남아 있는 Kimi 공식 OAuth 항목은 공급자 페이지에서 보호되며, 네이티브 항목을 제거한 뒤 저장된 프로필을 삭제할 수 있습니다.

> **참고**: 처음 실행하면 기존 Claude Code, Codex, Gemini CLI, Grok Build 설정을 `default`라는 공급자로 자동으로 가져옵니다. 또한 이 도구들과 Claude Desktop에 각각 공식 공급자를 추가하므로 기존 설정을 잃지 않습니다.

각 기능의 자세한 사용법은 **[사용자 매뉴얼 (영문)](docs/user-manual/en/README.md)**을 참고하세요. 공급자 관리, MCP/프롬프트/Skills, 로컬 라우팅 및 장애 조치 등을 설명합니다.

<a id="features"></a>

## 주요 기능

[전체 변경 이력](CHANGELOG.md) | [v4.0 릴리스 노트 (영문)](docs/release-notes/v4.0.4-en.md)

<a id="supported-features-by-tool"></a>

### 도구별 지원 기능

| 도구                                          | 공급자 |   로컬 라우팅    | 통합 | 트레이 전환 | MCP | Skills | 프롬프트                              | 세션 |    사용 통계     |
| --------------------------------------------- | ------ | :--------------: | :--: | :---------: | :-: | :----: | ------------------------------------- | :--: | :--------------: |
| Claude Code                                   | 전환   |        ✓         |  ✓   |      ✓      |  ✓  |   ✓    | CLAUDE.md                             |  ✓   |        ✓         |
| Claude Desktop                                | 전환   | 모델 매핑만 지원 |  –   |      ✓      |  –  |   –    | –                                     |  –   | 모델 매핑만 지원 |
| Codex                                         | 전환   |        ✓         |  ✓   |      ✓      |  ✓  |   ✓    | AGENTS.md                             |  ✓   |        ✓         |
| Gemini CLI                                    | 전환   |        ✓         |  –   |      ✓      |  ✓  |   ✓    | GEMINI.md                             |  ✓   |        ✓         |
| Grok Build                                    | 전환   |        ✓         |  –   |      ✓      |  ✓  |   ✓    | AGENTS.md                             |  ✓   |        ✓         |
| OpenCode                                      | 공존   |        –         |  –   |      –      |  ✓  |   ✓    | AGENTS.md                             |  ✓   |        ✓         |
| OpenClaw                                      | 공존   |        –         |  –   |      –      |  –  |   –    | 작업 공간 편집기                      |  ✓   |        –         |
| Hermes                                        | 공존   |        –         |  –   |      –      |  ✓  |   ✓    | 메모리                                |  ✓   |        –         |
| Pi                                            | 공존   |        –         |  –   |      –      |  ✓  |   ✓    | AGENTS.md, SYSTEM.md, 프롬프트 템플릿 |  ✓   |        ✓         |
| MiniMax Code                                  | 공존   |        –         |  –   |      –      |  ✓  |   ✓    | AGENTS.md                             |  ✓   |        ✓         |
| [Kimi Code](docs/kimi-code-integration-zh.md) | 공존   |        –         |  –   |      –      |  ✓  |   ✓    | AGENTS.md                             |  ✓   |        ✓         |
| Oh My Pi                                      | 공존   |        –         |  –   |      –      |  ✓  |   ✓    | AGENTS.md                             |  ✓   |        –         |

- **전환**: 한 번에 하나의 공급자만 활성화합니다. **공존**: 여러 공급자를 도구 자체 설정에 동시에 저장하고 도구 안에서 선택해 사용합니다.
- **로컬 라우팅**: CC Switch가 로컬 컴퓨터에서 요청을 전달하고 API 형식을 변환합니다. 아래 [로컬 라우팅 및 장애 조치](#local-routing--failover)를 참고하세요. Claude Desktop 공급자는 "직접 연결" 또는 "모델 매핑"을 사용할 수 있으며, "모델 매핑"에서는 로컬 라우팅을 거칩니다.
- **통합**: 여러 공급자의 모델을 하나의 모델 목록에 모으며 선택한 모델의 공급자로 요청을 보냅니다. 아래 [통합 모드](#aggregation-mode)를 참고하세요.
- **세션**: 대화 기록을 찾아보고 검색하거나 읽기 화면을 열고, 재개 명령을 복사해 대화를 이어갈 수 있습니다. OpenClaw와 Hermes는 아직 세션 재개를 지원하지 않습니다. Hermes는 최근 세션 500개만 표시합니다.
- **사용 통계**: 로컬 라우팅을 사용하지 않아도 각 도구의 로컬 세션 로그에서 사용량을 수집합니다. 로컬 라우팅을 거치는 요청도 집계합니다.
- Claude Desktop 페이지에서 여는 MCP, Skills, 프롬프트, 세션 패널은 Claude Code에 적용됩니다.

### 공급자 관리

- **90개 이상의 공급자 프리셋** — 프리셋을 선택하고 키를 입력해 공급자를 추가하거나 사용자 정의 설정을 만듭니다. 추가 패널에서 이름(중국어 이름 포함)과 도메인으로 검색할 수 있으며, 같은 서비스의 여러 요금제와 리전은 한 행에 모아 표시합니다.
- **핵심 필드만 변경** — 전환 시 엔드포인트, 키, 모델 등 연결 정보만 바뀝니다. 플러그인, Hooks, MCP, 직접 추가한 설정과 주석은 그대로 유지됩니다. 편집기는 전환 후의 설정 파일 모습을 보여 주며, CC Switch가 각 설정 파일을 처음 덮어쓰기 전에 자동으로 백업합니다.
- **프로젝트** — Claude Code 또는 Codex의 현재 공급자, MCP, Skills, 프롬프트 파일을 프로젝트로 저장하고, 페이지 상단의 프로젝트 전환기나 트레이에서 클릭 한 번으로 전체 구성을 전환합니다. Claude Desktop에서는 공급자만 저장합니다. 다른 프로젝트로 전환할 때 현재 상태는 이전 프로젝트에 자동으로 저장됩니다. 프로젝트 전환기는 기본적으로 숨겨져 있으며 "설정 → 일반"의 "프로젝트 전환기 표시"에서 켤 수 있습니다.
- **인증 센터 (베타)** — 사이드바의 "인증 센터"에서 여러 GitHub Copilot, ChatGPT, xAI (Grok) 계정으로 로그인하고 해당 구독을 Claude Code, Claude Desktop, Codex의 공급자로 사용할 수 있습니다. Codex의 OpenAI Official을 제외하면 모두 라우팅 모드가 필요합니다. 공식 클라이언트 외부에서 구독을 사용하는 행위는 서비스 제공자의 이용약관을 위반할 수 있으므로 위험을 직접 판단하세요.
- **Claude Desktop용 타사 공급자** — Anthropic 호환 엔드포인트에 직접 연결할 수 있습니다. Claude 외의 모델은 "모델 매핑"을 선택해 Sonnet, Opus, Haiku 등의 등급을 공급자의 실제 모델에 매핑하며, 요청은 로컬 라우팅을 거칩니다.
- **범용 공급자** — 하나의 설정을 Claude Code, Codex, Gemini CLI에 동기화합니다.
- 클릭 한 번으로 전환, 시스템 트레이에서 빠른 전환(Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build), 드래그 정렬, 가져오기/내보내기

<a id="local-routing--failover"></a>

### 로컬 라우팅 및 장애 조치

- **API 형식 변환** — Anthropic Messages, OpenAI Chat Completions, OpenAI Responses, Gemini Native 간 요청을 변환합니다. Claude Code와 Claude Desktop에서 OpenAI 또는 Gemini 형식의 공급자를, Codex와 Grok Build에서 Chat Completions 또는 Anthropic Messages 공급자를 사용할 수 있습니다.
- **도구별 활성화** — Claude Code, Codex, Gemini CLI, Grok Build는 각각 별도로 라우팅 모드에 들어갈 수 있습니다. 페이지 상단의 "라우팅" 탭에서 "라우팅 시작"을 클릭하세요. 라우팅 모드에서는 공급자를 전환하면 이후 요청에 즉시 적용됩니다. 단, Codex, Gemini CLI, Grok Build에서 모델이 바뀌면 재시작이 필요할 수 있습니다. CC Switch를 종료하면 먼저 직접 연결 설정을 복원하고 다음 실행 시 다시 라우팅에 연결합니다.
- **자동 장애 조치** — 도구별 장애 조치 대기열을 구성합니다. 요청에 실패하면 회로 차단기와 공급자 상태 모니터링을 바탕으로 대기열의 다음 공급자로 자동 전환합니다.
- **호환성 보정** — 일부 업스트림에서 처리하지 못하는 요청을 자동으로 보정합니다. 예: 추론 서명 문제, 이미지 미지원 시 대체 처리.
- 공식 공급자(예: Claude Official)는 로컬 라우팅을 사용할 수 없습니다. Codex의 OpenAI Official은 예외입니다.
- 라우팅 서비스 상태, 수신 주소, 장애 조치 설정은 모두 "설정 → 로컬 라우팅"에서 관리합니다.
- 가이드: [Claude Code에서 GPT 사용하기 (영문)](docs/guides/claude-codex-routing-guide-en.md) · [Codex에서 Claude 사용하기 (영문)](docs/guides/codex-claude-routing-guide-en.md)

<a id="aggregation-mode"></a>

### 통합 모드

- **하나의 모델 목록에 여러 공급자** — Claude Code 또는 Codex 페이지에서 "통합"로 전환한 뒤 공급자를 추가하면 해당 모델이 클라이언트의 모델 선택기에 표시됩니다. 요청은 선택한 모델의 공급자로 전달되므로 CC Switch에서 매번 전환할 필요가 없습니다.
- **언제든 추가 및 제거** — 공급자 카드에서 "추가" 또는 "제거"를 클릭하고 공급자 하나를 기본값으로 지정합니다. 통합 모델을 명시하지 않은 요청은 기본 공급자로 전달됩니다. Codex의 OpenAI Official은 기본 공급자로만 사용할 수 있으며, Claude 공식 구독은 현재 통합을 지원하지 않습니다.
- **참고 사항** — 통합은 장애 조치를 제공하지 않습니다. Claude Code 2.1.243 이상이 필요합니다. 통합 목록을 변경하면 Codex는 재시작해야 하지만 Claude Code는 그럴 필요가 없습니다. 세션 안에서 모델을 바꾸면 새 모델이 프롬프트 캐시를 다시 구성하므로 첫 턴에 비용이 조금 더 듭니다.
- 통합 모드의 설계는 [opencodex](https://github.com/lidge-jun/opencodex)를 많이 참고했습니다. 작성자와 기여자 여러분께 감사드립니다.
- 문서: [통합 모드 매뉴얼 (영문)](docs/user-manual/en/4-proxy/4.6-aggregation.md) · [그림으로 보는 가이드 (중문)](docs/guides/aggregation-mode-guide-zh.md)

### MCP, 프롬프트, Skills

- **통합 MCP 패널** — 모든 MCP 서버를 한곳에서 관리하고 서버마다 동기화할 도구를 선택합니다. Claude Code, Codex, Gemini CLI, Grok Build, OpenCode, Hermes, Pi, MiniMax Code, Kimi Code, Oh My Pi를 지원하며, 도구별 기존 설정 가져오기와 Deep Link 가져오기도 지원합니다.
- **프롬프트** — Markdown 편집기를 갖춘 도구별 프롬프트 라이브러리입니다. 활성화하면 해당 도구의 프롬프트 파일(CLAUDE.md / AGENTS.md / GEMINI.md)에 저장합니다. 저장 전에 파일의 기존 내용을 라이브러리에 보관하므로 내용이 사라지지 않습니다. Pi에서는 SYSTEM.md, APPEND_SYSTEM.md, 프롬프트 템플릿도 편집할 수 있습니다.
- **Skills** — skills.sh에서 검색하거나 GitHub 저장소 또는 ZIP 파일에서 클릭 한 번으로 설치할 수 있습니다. 업데이트를 확인하고 한 번에 모두 업데이트할 수 있습니다. 도구별 동기화 방식은 자동, 심볼릭 링크만 사용, 복사만 사용 중 선택하며, 저장 위치를 `~/.agents/skills`로 지정할 수도 있습니다.
- 세 패널 모두 검색을 지원합니다. MCP와 Skills는 도구별로 한 번에 모두 활성화하거나 비활성화할 수 있습니다. 공급자, MCP 서버, 프롬프트는 콘텐츠 영역의 전체 페이지에서 편집하며, 저장하지 않은 변경 사항이 있으면 페이지를 떠나기 전에 알려 줍니다.

### 사용량 및 비용 추적

- **사용량 대시보드** — 로컬 라우팅 없이도 동작합니다. 기본적으로 각 도구의 로컬 세션 로그를 자동으로 스캔해 공급자별·모델별 요청 수, 토큰, 캐시 적중률, 출력 속도, 비용을 추적합니다. 추이 차트, 연간 히트맵, 개별 요청 로그를 제공합니다.
- **할당량 및 잔액** — 공급자 카드와 트레이에서 잔여량과 초기화까지 남은 시간을 확인할 수 있습니다(예: "5시간 94% 남음"). 공식 구독 할당량(Claude, ChatGPT, Gemini, SuperGrok), Coding Plan의 5시간/주간/월간 할당량(Kimi, Zhipu GLM, MiniMax, Volcengine Ark 등), 계정 잔액(DeepSeek, OpenRouter, SiliconFlow 등)을 지원합니다. 일부 공급자는 카드의 "사용량 조회 설정"에서 먼저 켜야 하며, 다른 공급자는 사용자 정의 사용량 스크립트를 작성할 수 있습니다. ChatGPT 구독은 남은 한도 초기화 횟수와 Codex Credits 잔액도 표시합니다.
- **사용자 정의 요금** — 모델별 요금을 직접 설정하거나 models.dev에서 가져옵니다.

### 세션 관리자 및 작업 공간

- **세션 읽기 화면** — 각 도구의 세션 로그를 구조화해 텍스트, 추론, 도구 호출, 도구 결과, 이미지를 구분하여 표시합니다. 각 작업 턴은 단계 수, 변경 파일 수, 실패 수를 담은 한 줄 요약으로 접을 수 있으며, 실패한 단계는 빨간색으로 표시됩니다. 오른쪽에는 대화 개요가 표시되고, 세션 내 검색, Markdown 내보내기, 개별 턴 또는 전체 대화 복사를 지원합니다.
- **목록 및 재개** — 프로젝트나 시간별로 묶고 제목, 디렉토리, 메시지, 세션 ID를 검색하거나 일괄 삭제할 수 있습니다. 재개 명령을 복사해 대화를 이어가며, macOS에서는 클릭 한 번으로 터미널에서 재개할 수 있습니다.
- **작업 공간 편집기** (OpenClaw) — 에이전트 파일(AGENTS.md, SOUL.md 등)과 일일 메모리를 편집합니다.
- **메모리** (Hermes) — Hermes의 MEMORY.md와 USER.md를 편집합니다.

### 시스템 및 플랫폼

- **클라우드 동기화** — WebDAV(Jianguoyun, Nextcloud, Synology NAS 등) 또는 S3 호환 스토리지(AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS 등)로 기기 간 동기화합니다. CC Switch 설정 디렉토리를 Dropbox, OneDrive, iCloud 같은 클라우드 드라이브 폴더에 둘 수도 있습니다.
- **CLI 도구 관리** — 사이드바의 "앱" 페이지에서 Claude Code, Codex 등 명령줄 도구의 현재 버전과 최신 버전을 확인하고, 클릭 한 번으로 설치·업그레이드·전체 업그레이드를 실행하며 중복 설치를 진단합니다. Windows에서는 WSL 내부 도구도 관리할 수 있습니다. 자세한 내용은 자주 묻는 질문을 참고하세요.
- **Deep Link** (`ccswitch://`) — 링크를 통해 공급자, MCP 서버, 프롬프트를 가져오거나 Skills 저장소를 추가할 수 있습니다. [온라인 생성기](https://ccswitch.io/deplink.html)에서 링크를 만들 수 있습니다. 사이트에 가져오기 버튼을 추가하려면 [연동 가이드 (영문)](https://github.com/farion1231/cc-switch/blob/main/docs/guides/deeplink-site-integration-guide-en.md)를 참고하세요.
- **내장 유틸리티** — Claude Code 첫 실행 확인 건너뛰기, AI 기여 표시 숨기기, VS Code Claude Code 확장 프로그램에 CC Switch의 공급자 전환 적용 등을 지원합니다.
- 어두운/밝은/시스템 테마, 시작 시 자동 실행, 자동 업데이트, 원자적 쓰기, 자동 백업("설정 → 데이터"에서 모든 백업의 위치와 사용 공간 확인), 다국어 지원(간체 중국어/번체 중국어/영어/일본어 및 커뮤니티 번역인 튀르키예어/한국어)

<a id="faq"></a>

## 자주 묻는 질문

<details>
<summary><strong>CC Switch는 어떤 AI 도구를 지원하나요?</strong></summary>

**Claude Code**, **Claude Desktop**, **Codex**, **Gemini CLI**, **Grok Build**, **OpenCode**, **OpenClaw**, **Hermes**, **Pi**, **MiniMax Code**, **Kimi Code**, **Oh My Pi**의 12개 도구를 지원합니다. 각 도구에 전용 공급자 프리셋과 설정 관리를 제공하며, 기능별 지원 여부는 [도구별 지원 기능](#supported-features-by-tool)을 참고하세요.

</details>

<details>
<summary><strong>공급자를 전환한 뒤 터미널을 재시작해야 하나요?</strong></summary>

도구에 따라 다릅니다.

- **Claude Code**: 공급자 설정을 즉시 반영하므로 재시작할 필요가 없습니다.
- **Codex, Gemini CLI, Grok Build**: 터미널 또는 CLI 도구를 재시작해야 적용됩니다. 전환 후 CC Switch가 안내합니다. 라우팅 모드에서는 즉시 새 공급자로 요청을 보내지만, 모델이 바뀌면 세 도구 모두 재시작이 필요할 수 있습니다.
- **통합 모드**: Claude Code의 통합 모델 변경은 즉시 적용됩니다. Codex는 통합 모드 진입·종료 또는 통합 모델 목록 변경 시 완전히 재시작해야 합니다. 다음 항목을 참고하세요.
- **Claude Desktop**: 앱을 완전히 종료한 뒤 다시 실행하세요. "모델 매핑"을 사용하는 동안에는 CC Switch도 실행 상태를 유지해야 합니다.
- **OpenCode, OpenClaw, Hermes, Pi, MiniMax Code, Kimi Code, Oh My Pi**: 공존 방식의 도구입니다. "추가"(Pi와 Oh My Pi는 "활성화")를 클릭하면 다른 공급자와 함께 도구 자체 설정에 저장되며, 도구 안에서 사용할 모델을 선택합니다. Kimi Code에는 공급자의 모델을 선택하는 "전환" 버튼도 있습니다. 주 모델 또는 서브에이전트 모델 풀에서 참조 중인 모델은 제거할 수 없습니다. 설정과 계정에 관한 자세한 내용은 [Kimi Code 연동 안내 (중문)](docs/kimi-code-integration-zh.md)를 참고하세요.

</details>

<details>
<summary><strong>통합 모드에서 Codex의 /model에 통합 모델이 표시되지 않는 이유는 무엇인가요?</strong></summary>

Codex는 시작할 때만 모델 목록을 읽습니다. 통합 모드에 진입하거나 종료한 뒤, 통합 공급자를 추가하거나 제거한 뒤, 또는 공급자의 통합 모델을 변경한 뒤에는 Codex를 완전히 재시작해야 새 목록이 표시됩니다.

- **Codex CLI**: 터미널을 닫고 `codex`를 다시 실행하는 것만으로는 충분하지 않습니다. 모든 터미널의 `codex`가 하나의 백그라운드 데몬을 공유하므로 새 목록을 읽으려면 데몬도 재시작해야 합니다. CC Switch가 이전 목록을 사용 중인 Codex를 감지하면 Codex 페이지 상단에 안내를 표시합니다. 안내의 "Codex 데몬 다시 시작"을 클릭하세요. 재시작하면 데몬에서 실행 중인 작업이 중단됩니다.
- **Codex 데스크톱 앱**: 완전히 종료한 뒤 다시 실행하세요. macOS에서는 ⌘Q를 누르세요. 창을 닫는 것만으로는 충분하지 않습니다.
- **편집기 확장 프로그램**: 편집기 창을 다시 여세요.

Claude Code는 영향을 받지 않습니다. 통합 모델 변경이 즉시 적용됩니다.

</details>

<details>
<summary><strong>공급자를 전환하면 플러그인, Hooks 또는 다른 설정도 바뀌나요?</strong></summary>

아니요. Claude Code, Codex, Gemini CLI, Grok Build에서 공급자를 전환하면 CC Switch는 설정 파일의 **핵심 필드**만 바꿉니다. 엔드포인트, 키, 모델 이름, API 프로토콜(Codex의 추론 강도, Gemini CLI의 인증 방식 포함), 공급자에 속하는 일부 호환성 옵션(Claude Code의 "Artifact Tool 비활성화", 컨텍스트 창 등)이 해당합니다. 플러그인, Hooks, 권한, MCP, 직접 추가한 환경 변수, 주석, 서식은 그대로 유지되며 모든 공급자에 공통으로 적용됩니다.

이러한 공통 설정은 도구 자체에서 바꾸거나 설정 파일을 직접 편집할 수 있습니다. CC Switch에서 아무 공급자나 편집해도 됩니다. 편집기는 "이 공급자로 전환한 뒤의 설정 파일 모습"을 보여 줍니다. 저장하면 핵심 필드는 해당 공급자에 저장되고, 나머지 변경 사항은 설정 파일에 기록되어 모든 공급자에 적용됩니다.

따라서 이전의 "공통 설정 스니펫"은 더 이상 필요하지 않아 관련 버튼이 제거되었습니다. 업그레이드 전 스니펫의 설정은 이전에 공급자를 전환할 때 이미 설정 파일에 기록되었으므로 그대로 남습니다. CC Switch가 각 설정 파일을 처음 덮어쓰기 전에는 원본을 `~/.cc-switch/backups/live-first-write/`에 백업합니다.

</details>

<details>
<summary><strong>도구 안에서 모델을 바꿨는데 다른 공급자로 전환했다가 돌아오면 왜 원래대로 되나요?</strong></summary>

모델은 공급자에 속하는 핵심 필드입니다. 도구 안에서 선택한 모델(예: Claude Code의 `/model`)은 다음 전환 전까지 유지됩니다. 공급자를 전환하면 설정 파일의 모델을 대상 공급자에 저장된 모델로 바꾸며, 도구 안에서 선택했던 모델을 이전 공급자에 저장하지 않습니다. 특정 모델을 계속 사용하려면 CC Switch에서 해당 공급자를 편집하세요.

이전 버전은 다른 공급자로 전환할 때 전체 설정 파일을 이전 공급자에 저장했습니다. 이제는 그렇게 하지 않습니다. 이 방식은 플러그인 등 공통 설정을 특정 공급자에 묶어 두어 다른 공급자로 전환하면 사라지게 만드는 문제가 있었기 때문입니다.

</details>

<details>
<summary><strong>현재 사용 중인 공급자를 삭제할 수 없는 이유는 무엇인가요?</strong></summary>

CC Switch는 앱을 삭제하더라도 각 도구가 정상적으로 동작하도록, 기존 환경에 미치는 영향을 최소화하는 설계 원칙을 따릅니다.

따라서 한 번에 하나의 공급자를 사용하는 도구(Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build)는 항상 사용 중인 설정 하나를 유지합니다. 모든 설정을 삭제하면 해당 도구를 사용할 수 없기 때문입니다. 삭제하려면 먼저 다른 공급자로 전환하세요. 통합 모드의 기본 공급자도 먼저 다른 공급자를 기본값으로 지정해야 제거할 수 있습니다. 공존 방식 도구(OpenCode, OpenClaw, Hermes, Pi, MiniMax Code)는 이 제한 없이 공급자를 바로 삭제할 수 있습니다. 자주 사용하지 않는 도구는 "앱" 페이지에서 사이드바에 표시되지 않도록 숨길 수 있습니다. 공식 로그인으로 돌아가는 방법은 다음 질문을 참고하세요.

</details>

<details>
<summary><strong>공식 로그인으로 어떻게 돌아가나요?</strong></summary>

CC Switch의 Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build 공급자 목록에는 각각 기본 제공 공식 공급자(**Claude Official**, **Claude Desktop Official**, **OpenAI Official**, **Google Official**, **Grok Official**)가 있습니다. 삭제했다면 프리셋에서 다시 추가하세요. 공식 공급자로 전환한 뒤 도구 자체의 로그인 절차(예: Claude Code의 `/login`, Codex의 `codex login`)를 따르세요. 이후 공식 공급자와 타사 공급자 사이를 자유롭게 전환할 수 있습니다.

Codex는 CC Switch 안에서 "ChatGPT로 로그인"을 사용해 여러 ChatGPT 계정으로 로그인할 수도 있습니다. **OpenAI Official** 카드마다 "사용할 계정"을 선택하면 여러 Plus, Pro, Team 계정을 클릭 한 번으로 전환할 수 있습니다. "Codex 로그인 따르기"로 설정한 카드는 Codex CLI 자체 로그인을 계속 사용합니다.

참고: 공식 구독은 도구 자체 로그인을 사용하며 로컬 라우팅을 거치지 않습니다. 라우팅 모드에서는 공식 공급자를 선택할 수 없습니다. Codex의 OpenAI Official 카드는 예외이며, 다른 공식 공급자를 사용하려면 먼저 직접 연결로 돌아가세요.

</details>

<details>
<summary><strong>라우팅을 시작하면 설정 파일의 주소가 127.0.0.1로 바뀌는 이유는 무엇인가요?</strong></summary>

라우팅 모드에서는 도구의 요청이 먼저 CC Switch의 로컬 라우팅(기본값: `http://127.0.0.1:15721`)으로 전달되고, CC Switch가 선택한 공급자로 전달합니다. 따라서 도구 설정 파일에는 로컬 주소와 자리표시자 키 `PROXY_MANAGED`만 기록됩니다. Claude Code는 모델 이름도 `claude-sonnet-5` 같은 고정 별칭으로 기록합니다. `/model` 메뉴에는 실제 모델 이름이 계속 표시됩니다. 실제 공급자 주소, 키, 모델은 모두 CC Switch에 저장됩니다. 통합 모드도 같은 방식으로 동작합니다.

사이드바의 "사용량"에 있는 요청 로그에서 각 요청의 "요청 모델 → 실제 모델"을 확인할 수 있습니다.

라우팅 모드에서 공급자를 전환하면 라우팅에 사용할 공급자가 바뀝니다. 라우팅 진입 전에 사용하던 공급자는 그대로 유지되며 카드에 "직접 연결"로 표시됩니다. "직접 연결로 돌아가기"를 클릭하면 이 공급자의 설정을 설정 파일에 복원합니다. CC Switch를 종료할 때도 먼저 직접 연결 공급자 설정을 복원하고, 다음 실행 시 다시 라우팅에 연결합니다.

</details>

<details>
<summary><strong>Claude Code에서 OpenAI 호환 API, Gemini 또는 로컬 모델을 사용할 수 있나요?</strong></summary>

가능하지만 라우팅이 필요합니다. 공급자를 편집할 때 "고급 옵션"의 "업스트림 형식"을 공급자의 API와 일치하도록 설정하세요. Chat Completions 엔드포인트만 제공하는 서비스(많은 로컬 모델 서버 포함)는 "OpenAI Chat Completions", Responses 엔드포인트를 제공하는 서비스는 "OpenAI Responses API", Gemini는 "Gemini Native generateContent"를 선택합니다. 그런 다음 Claude Code 페이지의 "라우팅" 탭에서 "라우팅 시작"을 클릭하세요. 형식이 맞지 않거나 라우팅을 시작하지 않으면 보통 404 또는 405 오류가 발생합니다.

반대로 Codex 또는 Grok Build에서 "업스트림 형식"을 "Anthropic Messages"로 선택하면 Claude 형식의 공급자를 사용할 수 있습니다. 이 경우에도 라우팅이 필요합니다. 자세한 내용은 [Claude Code에서 GPT 사용하기 (영문)](docs/guides/claude-codex-routing-guide-en.md)와 [Codex에서 Claude 사용하기 (영문)](docs/guides/codex-claude-routing-guide-en.md)를 참고하세요.

</details>

<details>
<summary><strong>"연결 확인"은 통과했는데 요청이 실패하는 이유는 무엇인가요?</strong></summary>

공급자 카드의 "연결 확인"은 공급자 주소에 접근할 수 있는지만 확인합니다. 실제 모델 요청은 보내지 않으므로 API 키와 모델 이름이 올바른지는 검증하지 못합니다. 요청에 실패하면 키, 모델 이름, 업스트림 형식을 확인하세요. 라우팅을 거치는 요청은 사이드바의 "사용량"에 있는 요청 로그에서 정확한 오류를 확인할 수 있습니다.

</details>

<details>
<summary><strong>데이터는 어디에 저장되나요?</strong></summary>

기본적으로 모든 데이터는 홈 디렉토리의 `.cc-switch` 폴더(Windows: `C:\Users\<user>\.cc-switch`)에 저장됩니다.

- **데이터베이스**: `cc-switch.db` (SQLite — 공급자, MCP, 프롬프트, Skills, 프로젝트, 사용 기록 등)
- **로컬 설정**: `settings.json` (도구별 설정 디렉토리, 백업 정책, 클라우드 동기화 연결 정보 등 기기별 설정)
- **백업**: `backups/` (기본적으로 24시간마다 자동 백업하며 최근 10개를 보관합니다. "설정 → 데이터 → 백업 및 복원"에서 조정할 수 있습니다. 아래의 "기타 백업"에는 다른 모든 백업의 위치와 크기가 표시되며 유형별로 정리할 수 있습니다.)
- **Skills**: `skills/` (설정에서 `~/.agents/skills`로 변경 가능). 기본적으로 심볼릭 링크로 도구에 동기화하며 실패하면 복사합니다.
- **Skills 백업**: `skill-backups/` (Skills 제거 또는 업데이트 전에 자동 생성하며 최근 20개를 보관합니다.)
- **OAuth 로그인 자격 증명**: `copilot_auth.json`, `codex_oauth_auth.json`, `xai_oauth_auth.json`
- **로그**: `logs/cc-switch.log`, `crash.log` — 문제를 제보할 때 첨부해 주세요.
- **기기 상태**: `live-state.json` (각 도구의 현재 직접 연결/라우팅/통합 모드와 마지막 기록 내용), `codex-login-stash.json` (타사 공급자로 전환할 때 따로 보관하고 공식 공급자로 돌아갈 때 복원하는 Codex 공식 로그인)
- **원본 설정 파일**: `backups/live-first-write/` (CC Switch가 처음 덮어쓰기 전의 도구별 설정 파일)

"설정 → 데이터 → 저장 위치"에서 "CC Switch 설정 디렉토리"를 변경하면 위 파일 중 `settings.json`, 기기 상태, 원본 설정 파일을 제외한 나머지는 새 디렉토리에 저장됩니다. CC Switch는 기존 파일을 자동으로 옮기지 않으므로 먼저 직접 복사하세요. `settings.json`, 기기 상태, 원본 설정 파일은 이 컴퓨터에만 속하며, 항상 기본 디렉토리에 남고 클라우드 동기화에도 포함되지 않습니다.

</details>

<details>
<summary><strong>Windows에서 WSL 내부의 도구를 어떻게 관리하나요?</strong></summary>

CC Switch는 WSL을 자동으로 감지하지 않습니다. "설정 → 앱 설정"에서 해당 도구의 설정 디렉토리를 `\\wsl.localhost\Ubuntu\home\<user>\.claude` 같은 WSL 내부 경로로 바꾸세요. 저장하면 WSL 내부 설정을 읽고 씁니다. Claude Code, Codex, Gemini CLI, Grok Build, OpenCode, OpenClaw, Hermes, Pi를 지원합니다. 설정을 마치면 사이드바의 "앱" 페이지에서도 해당 WSL 배포판 안의 도구를 감지하고 업그레이드합니다.

참고: 라우팅과 통합은 설정 파일에 `127.0.0.1`을 주소로 기록합니다. WSL2의 기본 NAT 네트워크 모드에서는 WSL 내부의 `127.0.0.1`로 Windows의 로컬 라우팅에 접근할 수 없습니다. WSL을 미러링 네트워크 모드로 전환하세요.

</details>

<details>
<summary><strong>명령줄 또는 헤드리스 버전이 있나요?</strong></summary>

CC Switch 자체는 그래픽 인터페이스가 필요한 데스크톱 앱으로만 제공됩니다. 시스템 요구 사항은 [다운로드 및 설치](#download--installation)를 참고하세요. 서버, SSH 세션, 데스크톱 환경이 없는 컴퓨터에는 커뮤니티가 관리하는 **[CC Switch CLI](https://github.com/SaladDay/cc-switch-cli)**를 권장합니다. 대화형 터미널 UI(TUI)와 명령줄 모드를 모두 제공하며 Claude Code, Codex, Gemini CLI, OpenCode, OpenClaw, Hermes, Pi를 지원합니다. Homebrew(`brew install cc-switch-cli`) 또는 설치 스크립트로 설치할 수 있습니다.

CC Switch CLI는 기본적으로 데스크톱 앱과 `~/.cc-switch` 데이터 디렉토리를 공유하며 데스크톱 앱의 WebDAV 동기화와 호환됩니다. 두 프로젝트는 별도로 릴리스되며 CLI가 지원하는 데이터베이스 버전이 데스크톱 앱보다 늦을 수 있습니다. "데이터베이스 버전이 너무 최신입니다"라는 메시지가 표시되면 CLI를 업그레이드하거나 지원될 때까지 기다려 주세요.

</details>

<details>
<summary><strong>Linux (Wayland + NVIDIA): 클릭이 되지 않고 창 크기를 바꾸면 화면이 검게 변해요</strong></summary>

AppImage는 과거 네이티브 Wayland의 충돌을 피하기 위해 `GDK_BACKEND=x11` (XWayland)을 강제합니다. 최신 Wayland + NVIDIA 환경에서는 이로 인해 웹 콘텐츠 영역의 클릭이 작동하지 않거나(제목 표시줄 버튼은 작동함), 크기를 바꿀 때 화면이 검게 변할 수 있습니다. 다음 환경 변수를 지정해 네이티브 Wayland로 실행할 수 있습니다.

```bash
CC_SWITCH_GDK_BACKEND=wayland ./CC-Switch-*.AppImage
```

바탕 화면 아이콘으로 실행한다면 `.desktop`의 `Exec=` 행에 추가하거나(예: `env CC_SWITCH_GDK_BACKEND=wayland /path/to/AppImage`) 세션 환경 변수로 설정하세요. 이 변수는 다른 환경에서도 사용할 수 있습니다. 타일링 Wayland 컴포지터(sway/Hyprland)에서 클릭이 작동하지 않으면 반대로 `CC_SWITCH_GDK_BACKEND=x11`을 시도해 보세요. 지정하지 않으면 기본 동작을 유지합니다.

</details>

더 많은 질문은 사용자 매뉴얼의 [자주 묻는 질문 (영문)](docs/user-manual/en/5-faq/5.2-questions.md)을 참고하세요.

## 기여하기

문제 제보와 제안을 환영합니다. 새 기능을 개발하기 전에는 먼저 이슈를 열어 구현 방향을 논의해 주세요. 프로젝트 방향에 맞지 않는 기능 PR은 닫힐 수 있습니다.

개발 환경 설정, 제출 전 점검, 아키텍처 설명은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요. 사용 관련 질문은 먼저 [SUPPORT.md](SUPPORT.md)를 확인하고, 보안 취약점은 [SECURITY.md](SECURITY.md)에 안내된 방법으로 비공개 제보해 주세요.

**기술 스택**: Tauri 2 · Rust · React 18 · TypeScript · SQLite

## Star 이력

[![Star History Chart](https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date)](https://www.star-history.com/#farion1231/cc-switch&Date)

## 라이선스

MIT © Jason Young
