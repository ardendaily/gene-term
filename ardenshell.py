'''

baaaaarebones interactive shell with function binding

'''
import sys

class ArdenShell:
	'''
	Container for IO and function binding
	'''
	def __init__(self):
		self.bindCommands = {}
		self.loopMethods = {}
		self.namespace = None
		self.exitText = "Bye!"
		self.pcresponse = ""
		self.err = "Command not found."
		self.banner = "Welcome" #displays once at start of program
		self.eBanner = "" #displays after every interaction.
		self.reticule = "> " #beckon input

	def setnamespace(self, namespace):
		self.namespace = namespace

	def userin(self, _input):
		''' Handle user input '''
		_input = _input.lower()
		_input = _input.split(" ")
		if _input[0] in self.bindCommands.keys():
			if len(_input) > 1:
				return self.bindCommands[_input[0]]( _input[1:])
			else:
				return self.bindCommands[_input[0]]()
		else:
			return self.err

	def die(self):
		print ""
		print ""
		print self.exitText
		exit()

	def bindCommand( self, comStrings, methString, namespace=sys.modules[__name__]):
		''' 
		construct table linking commands to 
		methods in program namespace 
		'''

		#accept either single key or list of keys
		if not isinstance( comStrings, list ):
			comStrings = [comStrings]
			
		for key in comStrings:
			methObject = getattr(namespace, methString)
			self.bindCommands[key] = methObject

	def addLoopMethod( self, methString, methArgs=None, namespace=sys.modules[__name__]):
		'''
		Append method to loop, exec in order. 
		'''

		self.loopMethods[methString] = {}

		methObject = getattr(namespace, methString)
		self.loopMethods[methString]['function'] = methObject
		
		args = []

		if methArgs is not None:
			if not isinstance(methArgs, list):
				methArgs = [methArgs]

			for argument in methArgs:
				#arguments are everything else
				args.append(argument)

		self.loopMethods[methString]['args'] = args

	def setBanner( self, banner):
		self.banner = banner

	def setErrorText( self, _errtext):
		self.err = _errtext

	def setExitText( self, _exittext):
		self.exitText = _exittext

	def loop(self, noIO=False):
		print ""
		print ""
		print self.banner
		print ""
		print ""

		while True:
			try:
				print self.pcresponse
				print self.eBanner

				for methArgs in self.loopMethods.keys():

					if len(self.loopMethods[methArgs]['args']) > 0 :
						self.loopMethods[methArgs]['function']( 
							self.loopMethods[methArgs]['args'] 
						)
					else:
						self.loopMethods[methArgs]['function']()
				if not noIO:
					user = raw_input(self.reticule)
					self.pcresponse = self.userin( user )
			except KeyboardInterrupt:
				# Catch 
				self.die()