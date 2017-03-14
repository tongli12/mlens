"""ML-ENSEMBLE

Exception handling classes
"""


class NotFittedError(ValueError, AttributeError):

    """Error class for not fitted ensembles."""


class FitFailedWarning(RuntimeWarning):

    """Warning for failed fitting."""


class FitFailedError(RuntimeError):

    """Error for failed fitting."""


class SliceError(TypeError, IndexError, ValueError, AttributeError):

    """Error class for failed slicing."""


class LayerSpecificationError(TypeError, ValueError):

    """Error class for incorrectly specified layers."""


class LayerSpecificationWarning(UserWarning):

    """Error class for incorrectly specified layers."""


class EfficiencyWarning(UserWarning):
    """Warning used to notify the user of inefficient computation.

    This warning notifies the user that the efficiency may not be optimal due
    to some reason which may be included as a part of the warning message.
    This may be subclassed into a more specific Warning class.

    .. versionadded:: 0.18

    .. note:: imported from Scikit-learn for validation compatibility
    """


class NonBLASDotWarning(EfficiencyWarning):
    """Warning used when the dot operation does not use BLAS.

    FROM SCIKIT-LEARN

    This warning is used to notify the user that BLAS was not used for dot
    operation and hence the efficiency may be affected.

    .. versionchanged:: 0.18
       Moved from sklearn.utils.validation, extends EfficiencyWarning.

    .. note:: imported from Scikit-learn for validation compatibility
    """


class DataConversionWarning(UserWarning):
    """Warning used to notify implicit data conversions happening in the code.

    This warning occurs when some input data needs to be converted or
    interpreted in a way that may not match the user's expectations.

    For example, this warning may occur when the user
        - passes an integer array to a function which expects float input and
          will convert the input
        - requests a non-copying operation, but a copy is required to meet the
          implementation's data-type expectations;
        - passes an input whose shape can be interpreted ambiguously.

    .. versionchanged:: 0.18
       Moved from sklearn.utils.validation.

    .. note:: imported from Scikit-learn for validation compatibility.
    """


class InputDataWarning(UserWarning):
    """Warning used to notify that an array does not behave as expected.

    Probably, this is because the data is held in an object not anticipated by
    the validation suite, and as such is likely to fail fitting.
    """