# Changelog

## 0.8.0 (2025-12-10)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/Alchemyst-ai/alchemyst-sdk-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** api update ([67f9147](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/67f9147bbb0eb3f144a3f3aaa7b718483f7b13b5))


### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([0b0833a](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/0b0833a2758c4e0715713a85ed199f24601f38a7))


### Chores

* add missing docstrings ([ae31a75](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/ae31a757dee2a63edf41456179883b40a52da924))

## 0.7.0 (2025-12-03)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/Alchemyst-ai/alchemyst-sdk-python/compare/v0.6.0...v0.7.0)

### Features

* **api:** api update ([4f8ed74](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/4f8ed74008c6829034ced6d26b922b3a319142e3))


### Bug Fixes

* **client:** close streams without requiring full consumption ([338aad1](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/338aad1501c8d322cf7f4bc9609e57ab7f06f03d))
* compat with Python 3.14 ([dbe25c4](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/dbe25c42b1712617a6a63d74f293e3293b7841d8))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([10d06c4](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/10d06c40a238d847b8beb036b462d2e087108c8a))
* ensure streams are always closed ([f591b89](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/f591b893de4ea0d77e3cb3792452c3bbab34cc62))


### Chores

* add Python 3.14 classifier and testing ([ab921a4](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/ab921a4e1385d40a649988e9b3e815ac5a991b6d))
* bump `httpx-aiohttp` version to 0.1.9 ([9421012](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/94210125a9c4d6a333d720d751a9c9d242b70ab5))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([25c5bac](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/25c5bac17325ecf0aab962c9e0b8a5ef41a40452))
* **docs:** use environment variables for authentication in code snippets ([c300c9e](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/c300c9e6c1ef2776a75158520c8ee2e88a84ee2d))
* **internal/tests:** avoid race condition with implicit client cleanup ([46f4d22](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/46f4d2289bb353f0a76e02852dfc8fcdae171108))
* **internal:** codegen related update ([efa3043](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/efa30430779a0557f3b87c2196146a0ba89b56a9))
* **internal:** grammar fix (it's -&gt; its) ([f006062](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/f006062e60a078a0858ad0febd9dfd1e3a587cf4))
* **package:** drop Python 3.8 support ([fb767f8](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/fb767f855bd458ac1685a7362a9469a0d010b73f))
* update lockfile ([086bf00](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/086bf001c0421909c5fbe9251c732ad57e31bb29))

## 0.6.0 (2025-10-29)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/Alchemyst-ai/alchemyst-sdk-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** manual updates ([2512789](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/2512789d20bdc320da062a5b752fdebd070fbfbb))
* **api:** manual updates ([cc4d4bd](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/cc4d4bd22e25e7f468743c8785a18f36bed2c50f))

## 0.5.0 (2025-10-29)

Full Changelog: [v0.0.1...v0.5.0](https://github.com/Alchemyst-ai/alchemyst-sdk-python/compare/v0.0.1...v0.5.0)

### Features

* **api:** api update ([8b6419b](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/8b6419b8d3645059c5231c4e14dd1fe46b6dd3d8))
* **api:** api update ([1be64d9](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/1be64d9cd19dc3df6d72ebb5b2496779e9b76424))
* **api:** api update ([2561f6c](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/2561f6c5d35bfa474858bab7ee03999c765bc7d6))
* **api:** manual updates ([fb63c26](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/fb63c269c64dea5e2881d557c81581056f21da05))
* **api:** manual updates ([d230e11](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/d230e11ea56f28969fc8b6a2c2e3f80890430b34))
* **api:** manual updates ([cf37f37](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/cf37f371698f25907a245a5db5dfd2663e1e4451))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([5ddd383](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/5ddd3838203c871a97ab101d0fa71755a3b835ef))
* do not install brew dependencies in ./scripts/bootstrap by default ([076ff5b](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/076ff5bb3bd43bd7c998a64fc5e7395eaaabdb27))
* **internal:** detect missing future annotations with ruff ([fac1c37](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/fac1c371e564ca90bc31cef5335c8285ef1ab92a))
* sync repo ([62de6e7](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/62de6e77fe0e2ea96813fec36c0e3f7eaa30ab9c))
* update SDK settings ([601825a](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/601825a483ca56ead67e7bc952ede6eb595e66f1))
* update SDK settings ([8369476](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/8369476293e115785102255d3cf1d702daf3140c))
* update SDK settings ([07f1747](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/07f1747979ce926f286592beca52748afdd79a11))
* update SDK settings ([be467f2](https://github.com/Alchemyst-ai/alchemyst-sdk-python/commit/be467f232ee161643d1a9ad804161598900d56ff))
