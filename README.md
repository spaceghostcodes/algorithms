# algorithms
📚 Collection of algorithms

## Index
-	Sorting
	- [Binary Search](https://github.com/estebanborai/algorithms/blob/master/algorithms/functions/binary_search/binary_search.py)

Algorithm | Type | Implementation | Explanation
--- | --- | --- | ---
Binary Search | Sorting | [Code](https://github.com/estebanborai/algorithms/blob/master/algorithms/functions/binary_search.py) | [Notebook](https://github.com/estebanborai/algorithms/blob/master/notebooks/binary_search.ipynb)

## Debbuging
Debbuging its possible using Visual Studio Code.
**Python**'s extension is required in order to use the debugger with Visual Studio Code.

The following is the configuration to run each module:
```javascript
// File: (...)/algorihtms/.vscode/launch.json
{
	"version": "0.2.0",
	"configurations": [
		{
			"name": "Python: Current File",
			"type": "python",
			"request": "launch",
			"program": "${file}",
			"console": "integratedTerminal",
			"env": {
				"PYTHONPATH": "${workspaceRoot}"
			},
		}
	]
}
```

## Testing
Testing is supported using Visual Studio Code.
Just run the tests using the `Test` panel.
