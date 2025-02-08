# Llamaparse

## Task

Extract and parse tables from spreadsheet files in a local-hosted LLM

* Lightweight
* Cross-compatibility
* Doesn't need to be standalone
    * External requirements should be limited
* Can be a CLI tool (though keep in mind it may be in GUI later)
* Doesn't have to remain in `.ocr`

### LLM Options:

* Llama 3 ([Github repo](https://github.com/meta-llama/llama3))
* Hugging Face repo hub ([homepage](https://huggingface.co/))

> Llama's README states that the main repo is deprecated, and a different model should be used. Options include:
> * [llama-models](https://github.com/meta-llama/llama-models)
> * [Purplellama](https://github.com/meta-llama/PurpleLlama)
>
> Other models listed in Llama's README are not relevant for this project.

### Hosting Options:

* Local host
    * Involves a localhost endpoint as well (server pointer may default to `127.0.0.1` or `localhost`)
* Non-local self host
    * Encryption options (RSA?)

## Questions

* Hardware limitations (PC, laptop, etc)
* Hosting option (may be both)
* Licensing
* Environment?
