# Contribution Guidelines

Thank you for considering contributing to the `drf-app`! We appreciate your interest in helping us make this project better. Please take a moment to review these guidelines before submitting your contributions.

## Code of Conduct

We adhere to a [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and respectful environment for all contributors. Please read and follow the guidelines outlined there.

## Getting Started

Before you can contribute, you’ll need to set up your development environment:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/youzarsiph/drf-app.git
   cd drf-app
   ```

2. **Set Up the Environment**:
   - Install Poetry if not already installed:

     ```bash
     pip install poetry
     ```

   - Install the project dependencies:

     ```bash
     poetry install
     ```

3. **Running the Application**:

   ```bash
   poetry run python app/main.py
   ```

4. **Code Formatting**:
   - Ensure all code is formatted with Black:

     ```bash
     poetry run black .
     ```

5. **Code Linting**:
   - Ensure all code is linted using Ruff:

     ```bash
     poetry run ruff .
     ```

## How to Contribute

### Reporting Issues

If you encounter a bug or have a feature request, please [open an issue](https://github.com/youzarsiph/drf-app/issues/new). When reporting:

- Provide a clear and detailed description of the issue.
- Include steps to reproduce the problem if applicable.
- Mention the version of the software and your operating system.

### Pull Requests

We welcome pull requests that address issues or implement new features. Before you start:

1. **Check for Open Issues**:
   - Ensure the issue you want to address has not already been addressed.

2. **Create a New Issue**:
   - If the issue does not exist, create a new one to describe the problem or the feature you plan to implement.

3. **Fork the Repository**:
   - Fork the repository to your GitHub account.

4. **Create a New Branch**:
   - Create a new branch for your changes:

     ```bash
     git checkout -b feature/your-feature-name
     ```

5. **Make Your Changes**:
   - Implement your changes in the new branch.

6. **Run Tests**:
   - Verify that all tests pass and that your changes do not introduce new issues.

7. **Commit Your Changes**:
   - Commit your changes with a descriptive message:

     ```bash
     git commit -m "Add new feature: your feature name"
     ```

8. **Push to Your Fork**:
   - Push your changes to your forked repository:

     ```bash
     git push origin feature/your-feature-name
     ```

9. **Create a Pull Request**:
   - Open a pull request to the original repository. Ensure you reference the issue number you are addressing.
   - Provide a clear description of what your pull request does and why it should be merged.

### Continuous Integration

We use GitHub Actions for continuous integration:

- **Code Style (Black)**: Checks if the code is formatted according to Black.
- **Code Linting (Ruff)**: Ensures the code adheres to the linting rules set by Ruff.

If your pull request does not pass these checks, please fix the issues and push the changes.

## Code Review

Once a pull request is opened, it will be reviewed by one or more maintainers. Please be patient and responsive to feedback to ensure your changes are merged efficiently.

## License

By contributing to the `drf-app`, you agree that your contributions will be licensed under the [MIT License](LICENSE).

## Support

For any questions or assistance, you can:

- Visit the [GitHub Discussions](https://github.com/youzarsiph/drf-app/discussions).
- Open an issue in the [Issues](https://github.com/youzarsiph/drf-app/issues) section.
- Reach out to the maintainers directly if necessary.

Thank you for your contributions! We look forward to working with you.
