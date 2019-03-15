import pytest
import project1
from project1 import redactor
def testname():
    name='Sudheer'
    redactedname=redactor.redact_names(name)
    assert len(redactedname)==len(name)

