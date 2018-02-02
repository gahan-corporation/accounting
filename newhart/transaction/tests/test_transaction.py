"""Test cases for the transaction class."""
import datetime

class TestTransaction(object):
    """Transaction test cases."""

    transaction = None

    def test_transaction_amount(self, transactions, transaction):
        """Test the amount is a float."""
        self.transaction = transaction
        for item in transactions:
            transaction.amount = item.get('amount')
            amount = transaction.transaction_amount()

            if not isinstance(amount, float):
                raise AssertionError()
            if not isinstance(transaction.amount, float):
                raise AssertionError()

    def test_transaction_left_account(self, transactions, transaction, accounts):
        """Test that the left account exists."""
        self.transaction = transaction
        for item in transactions:
            transaction.left_account = item.get('left_account')
            left_account = transaction.transaction_left_account()
            if not isinstance(left_account, str):
                raise AssertionError()
            if left_account not in [
                    account.get('name') for account in accounts]:
                raise AssertionError()
            if transaction.left_account not in [
                    account.get('name') for account in accounts]:
                raise AssertionError()
            if not isinstance(item, dict):
                raise AssertionError()

    def test_transaction_right_account(self, transactions, transaction, accounts):
        """Test the right account exists."""
        self.transaction = transaction
        for item in transactions:
            transaction.right_account = item.get('right_account')
            right_account = transaction.transaction_right_account()

            if right_account not in [
                    account.get('name') for account in accounts]:
                raise AssertionError()
            if not isinstance(right_account, str):
                raise AssertionError()
            if transaction.right_account not in [
                    account.get('name') for account in accounts]:
                raise AssertionError()
            if not isinstance(item, dict):
                raise AssertionError()

    def test_transaction_date(self, transactions, transaction):
        """Test that the date is correctly formatted."""
        self.transaction = transaction
        for item in transactions:
            transaction.date = item.get('date')
            t_date = transaction.transaction_date()

            if not isinstance(t_date, datetime.date):
                raise AssertionError()
            if not isinstance(transaction.date, datetime.date):
                raise AssertionError()

    def test_transaction_description(self, transactions, transaction):
        """Test the description of the transaction."""
        self.transaction = transaction
        for item in transactions:
            transaction.description = item.get('description')
            description = transaction.transaction_description()

            if not isinstance(description, str):
                raise AssertionError()
            if not isinstance(transaction.description, str):
                raise AssertionError()
            if description != transaction.description:
                raise AssertionError()

    def test_transaction_tid(self, transactions, transaction):
        """Test that a tid is returned."""
        self.transaction = transaction
        for item in transactions:
            transaction.tid = item.get('tid')
            tid = transaction.transaction_tid()

            if not isinstance(tid, int):
                raise AssertionError()
            if not isinstance(transaction.tid, int):
                raise AssertionError()
            if tid != transaction.tid:
                raise AssertionError()
