const { execFileSync } = require("child_process");

class CustomProvider {
  id() {
    return "huggingface-local";
  }

  async callApi(prompt) {

    const result = execFileSync(
      "python",
      ["main.py", prompt],
      { encoding: "utf-8" }
    );

    return {
      output: result
    };
  }
}

module.exports = CustomProvider;