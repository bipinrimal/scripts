
{CompositeDisposable,File,Directory} = require 'atom'

module.exports = MarkdownImgHelper =

	activate: (state) ->
		atom.commands.onWillDispatch (e)  =>
			if e.type is "core:paste"

				editor = atom.workspace.getActiveTextEditor()
				return unless editor
				grammar = editor.getGrammar()
				return unless grammar
				return unless grammar.scopeName is 'source.gfm'


				clipboard = require 'clipboard'
				img = clipboard.readImage()

				return if img.isEmpty()

				e.stopImmediatePropagation()

				imgbuffer = img.toPNG()

				thefile = new File(editor.getPath())
				assetDir = "#{thefile.getBaseName().replace(/\.\w+$/, '').replace(/\s+/g,'')}"
				assetsDirPath = "#{thefile.getParent().getPath()}/#{assetDir}"



				crypto = require "crypto"
				md5 = crypto.createHash 'md5'
				md5.update(imgbuffer)

				filename = "#{thefile.getBaseName().replace(/\.\w+$/, '').replace(/\s+/g,'')}-#{md5.digest('hex').slice(0,5)}.png"

				@createDirectory assetsDirPath, ()=>
					@writePng assetsDirPath+'/', filename, imgbuffer, ()=>
						# ascClip = "assets/#{filename}"
						# clipboard.writeText(ascClip)

						@insertUrl "![](#{assetDir+'/'+filename})",editor

				return false

	createDirectory: (dirPath, callback)->
		assetsDir = new Directory(dirPath)

		assetsDir.exists().then (existed) =>
			if not existed
				assetsDir.create().then (created) =>
					if created
						console.log 'Success Create dir'
						callback()
			else
				callback()

	writePng: (assetsDir, filename, buffer, callback)->
		fs = require('fs')
		fs.writeFile assetsDir+filename, buffer, 'binary',() =>
			console.log('finish clip image')
			callback()

	insertUrl: (url,editor) ->
		editor.insertText(url)


	deactivate: ->


	serialize: ->
