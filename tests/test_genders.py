import pytest
import project1
from project1 import redactor
def testgender():
    name='women'
    redactedname=redactor.redact_genders(name)
    assert len(redactedname)-1==len(name)
