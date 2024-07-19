module.exports = {
  preset: 'ts-jest',
  testEnvironment: "jsdom",
  verbose: true,
  setupFilesAfterEnv: ["@testing-library/jest-dom/extend-expect"],
};