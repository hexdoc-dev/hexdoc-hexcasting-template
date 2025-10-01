# hexdoc-hexcasting-template
Copier template for adding a hexdoc plugin to a Hex Casting addon.

## Setting up a new plugin for an existing mod

### Copying the template

* Install the prerequisites:
   - [Git](https://github.com/git-guides/install-git)
   - [uv](https://docs.astral.sh/uv/getting-started/installation/)
* In your mod's Git repository, run this command to copy the template, then follow the prompts to set it up:
   ```sh
   uvx copier copy gh:hexdoc-dev/hexdoc-hexcasting-template .
   ```
* Use your editor's Git diff tool to review any files overwritten by the template (eg. `.gitignore`). All of the files in the template are there for good reasons, but you might want to merge some of your existing content into them.
* Set up your Python environment and lockfile:
   ```sh
   uv sync

   .\.venv\Scripts\activate   # Windows
   . .venv/bin/activate.fish  # fish
   source .venv/bin/activate  # everything else
   ```
* Commit the newly added files, including `uv.lock`.
* Try running `hexdoc serve`. Fix any errors you find.
  * Make sure to double-check the file paths and pattern regex in `doc/hexdoc.toml`.

### Setting up Pages

Follow these steps to set up GitHub Pages: https://hexdoc.hexxy.media/docs/guides/deployment/github-pages

### Setting up a PyPI account (optional, but highly recommended)

PyPI is the main Python package repository (like Node's NPM). hexdoc plugins are designed to be published to PyPI when you release new versions of your mod - think of it like just another place your mod is released to, alongside CurseForge and Modrinth.

* [Create a PyPI account](https://pypi.org/account/register/).
* Follow [these steps](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) to configure a pending publisher for your plugin.
  * PyPI Project Name: The `name` value from your pyproject.toml (eg. `hexdoc-yourmodid`).
  * Workflow name: `build_docs.yml`
  * Environment name: `pypi`
* Go to your GitHub repo settings > Environments, and create an environment called `pypi`.
* Try releasing the plugin to PyPI by manually running the `build_docs.yml` workflow from the Actions tab. By default, your mod is only released to PyPI when you manually run the release workflow like this, but you can also configure it to release automatically when certain conditions are met.

The default version number for your plugin is `1.0`. You can update this version by editing `doc/src/hexdoc_yourmodid/__version__.py`.

### Next steps

* Read through the files added by the template - make sure you know what you just added to your mod!
* If you use VSCode, consider installing the recommended extensions for auto-formatting, linting, and type checking.
* For more hexdoc examples, take a look at these projects:
  * [hexdoc](https://github.com/hexdoc-dev/hexdoc)
  * [hexdoc-hexcasting](https://github.com/FallingColors/HexMod)
  * [hexdoc-hexdebug](https://github.com/object-Object/HexDebug)

## FAQ

### Why should I publish my plugin to PyPI?

* It allows other hexdoc plugins to use content from your mod.
  * [hexdoc-hexcasting](https://pypi.org/project/hexdoc-hexcasting/) and [hexdoc-minecraft](https://pypi.org/project/hexdoc-minecraft/) are two hexdoc plugins that your web book already depends on.
* Publishing to PyPI will eventually be **mandatory** if you want your mod to be supported by [HexBug](https://github.com/object-Object/HexBug), [vscode-hex-casting](https://github.com/object-Object/vscode-hex-casting), or the [Book of Hexxy](https://book.hexxy.media).
