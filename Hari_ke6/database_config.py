"""
Database Configuration Module
Using python-dotenv for secure credential management

Author: Puspa
Date: April 26, 2026
Purpose: Demonstrate best practices for environment variables
"""

import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()


class DatabaseConfig:
    """
    Secure database configuration using environment variables.
    
    This class demonstrates best practices for managing database
    credentials without hardcoding sensitive information.
    """
    
    def __init__(self):
        """Initialize database configuration from environment variables."""
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = int(os.getenv('DB_PORT', 5432))
        self.database = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database_url = os.getenv('DATABASE_URL')
    
    def validate(self) -> bool:
        """
        Validate that all required environment variables are set.
        
        Returns:
            bool: True if configuration is valid
            
        Raises:
            ValueError: If required variables are missing
        """
        if self.database_url:
            # If DATABASE_URL is provided, that's sufficient
            return True
        
        # Otherwise, check individual components
        required_fields = {
            'database': self.database,
            'user': self.user,
            'password': self.password
        }
        
        missing = [field for field, value in required_fields.items() if not value]
        
        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing).upper()}\n"
                f"Please check your .env file."
            )
        
        return True
    
    def get_connection_string(self, hide_password: bool = True) -> str:
        """
        Generate database connection string.
        
        Args:
            hide_password: Whether to hide password in output (default: True)
            
        Returns:
            str: PostgreSQL connection string
        """
        if self.database_url:
            if hide_password:
                # Hide password in connection string
                parts = self.database_url.split('@')
                if len(parts) > 1:
                    user_pass = parts[0].split('//')[-1]
                    if ':' in user_pass:
                        user = user_pass.split(':')[0]
                        return f"postgresql://{user}:****@{parts[1]}"
            return self.database_url
        
        password = '****' if hide_password else self.password
        return f"postgresql://{self.user}:{password}@{self.host}:{self.port}/{self.database}"
    
    def display_config(self) -> None:
        """Display current configuration (safely, without exposing secrets)."""
        print("\n" + "="*60)
        print("DATABASE CONFIGURATION")
        print("="*60)
        print(f"Host:          {self.host}")
        print(f"Port:          {self.port}")
        print(f"Database:      {self.database or 'Not set'}")
        print(f"User:          {self.user or 'Not set'}")
        print(f"Password:      {'*' * 10 if self.password else 'Not set'}")
        print(f"Connection:    {self.get_connection_string(hide_password=True)}")
        print("="*60 + "\n")


def test_connection():
    """
    Test database configuration.
    
    This function demonstrates how to use the DatabaseConfig class
    and validate environment variables.
    """
    try:
        # Create configuration instance
        config = DatabaseConfig()
        
        # Validate configuration
        config.validate()
        
        # Display configuration
        config.display_config()
        
        print("✅ SUCCESS: Database configuration is valid!")
        print("✅ All required environment variables are set.")
        print("\n💡 TIP: In production, you would now use this config to")
        print("   establish an actual database connection using libraries")
        print("   like psycopg2, SQLAlchemy, or Django ORM.")
        
        return True
        
    except ValueError as e:
        print("\n❌ CONFIGURATION ERROR:")
        print(f"   {str(e)}")
        print("\n📝 TO FIX:")
        print("   1. Copy .env.example to .env")
        print("   2. Edit .env with your actual credentials")
        print("   3. Make sure .env is in your .gitignore")
        print("   4. Run this script again")
        return False
    
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {str(e)}")
        return False


if __name__ == "__main__":
    # Run test when script is executed directly
    print("🔐 Testing Database Configuration with Dotenv\n")
    test_connection()
