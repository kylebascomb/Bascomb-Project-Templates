# Using Pytest
Pytest is the go to testing library for python.

## Installing Pytest
You can add pytest to your project as detailed in the "Adding Dev / Tewst dependencies to a Poetry Project" section above:
``poetry add pytest --group dev``

## Writing Tests:

### Using @pytest.mark.parametrize
The @pytest.mark.parametrize is used to parametrize several inputs to a single function. An example is shown below:

``
@pytest.mark.parametrize(
    "test_input, expected",
    [(10, True), (11, False), (0, True), (-1, False), (-2, True)],
)
def test_even_odd(test_input, expected):
    number = EvenOddNumber(test_input)
    assert number.num_is_even() == expected
``

### Using @pytest.mark.skip
Marking a function as skip simply means that the test will be skipped when running the pytest command.

### Using @pytest.mark.xfail
Marking a function as xfail means that is is expected to fail.

### Using Pytest with exceptions
`` with pytest.raises(ValueError): ``

### Using fixtures
Fixtures are a way to duplicate code across tests
TODO


## Using Pytest
While in the Poetry Environment, you can run all your pytests using the ``pytest`` command in the terminal. This will run all functions in the directory that are prepended with 'test_' and located in a file that is prepended with 'test_'

# Coverage Tests

### Using pytest-cov for Coverage tests
We can install a package called pytest-cov to monitor the coverage of the pytests over the source code. First we have to install pytest-cov

poetry add pytest-cov --group dev


To run pytest-cov, you run your pytest script with the --cov="source code folder" and "/tests" to specify your test directory. See example below:

```pytest --cov=poetry_template tests/```
