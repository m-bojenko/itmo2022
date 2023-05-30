class Error(Exception):
    """ Базовый класс для всех исключений """
    pass


class EmptyEnter(Error):
    """ Вызывается, когда одно из обязательных полей пустое """
    pass


class IncorrectCarNumber(Error):
    """ Вызывается, когда введен некорректный номер ТС """
    pass


class NoDigitsError(Error):
    """ Вызывается, когда ввели некорректный ответ """
    pass


class TooBigNumber(Error):
    """ Вызывается, когда ввели слишком большое число """
    pass
