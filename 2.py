namespace Bank.WebApi.Models
{
    public class BankAccount
    {
        private readonly string m_customerName;
        private double m_balance;

        private BankAccount() { }

        public BankAccount(string customerName, double balance)
        {
            m_customerName = customerName ?? throw new ArgumentNullException(nameof(customerName));
            m_balance = balance;
        }

        public string CustomerName => m_customerName;
        public double Balance => m_balance;

        public void Debit(double amount)
        {
            ArgumentOutOfRangeException.ThrowIfGreaterThan(amount, m_balance);
            ArgumentOutOfRangeException.ThrowIfNegative(amount);

            m_balance -= amount;
        }

        public void Credit(double amount)
        {
            ArgumentOutOfRangeException.ThrowIfNegative(amount);

            m_balance += amount;
        }

    }
}
