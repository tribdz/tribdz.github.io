# Student Portfolio Template

This project gives you a personal portfolio website that you can edit and publish for free with GitHub Pages. You do not need to understand React or TypeScript to change your profile, education, projects, photos, writing, or resume.

## Quick Start

You need:

- [Node.js LTS](https://nodejs.org/en/download), which includes npm.
- [Git](https://git-scm.com/downloads), unless you download the project as a ZIP file.
- A text editor such as [Visual Studio Code](https://code.visualstudio.com/).
- A modern web browser.

Open a terminal in the project folder and run:

```bash
npm install
npm run dev
```

Open the local address printed in the terminal, usually `http://localhost:5173/`. Keep the terminal open while editing. The browser refreshes after you save a file.

Press `Ctrl+C` in the terminal to stop the local website.

## Install the Tools

Choose the instructions for your computer.

### Windows

1. Install [Git for Windows](https://git-scm.com/install/windows).
2. Install the **LTS** version of [Node.js](https://nodejs.org/en/download).
3. Close and reopen PowerShell, Command Prompt, or the VS Code terminal.

You can also use WinGet in PowerShell:

```powershell
winget install --id Git.Git -e --source winget
winget install --id OpenJS.NodeJS.LTS -e --source winget
```

### macOS

1. Install the **LTS** version of [Node.js](https://nodejs.org/en/download).
2. Open Terminal and install Apple's Git tools:

```bash
xcode-select --install
```

Close and reopen Terminal after installation.

### Linux, WSL, or ChromeOS

Install Git with your Linux package manager. On Ubuntu or Debian:

```bash
sudo apt update
sudo apt install git
```

Install the current Node.js LTS release with a version manager such as [nvm](https://github.com/nvm-sh/nvm):

```bash
nvm install --lts
nvm use --lts
```

For WSL, keep the project in your Linux home folder and install Git and Node inside WSL. On ChromeOS, first enable the Linux development environment. A school-managed Chromebook may require administrator help.

### Check the Installation

Run:

```bash
git --version
node --version
npm --version
```

This project requires Node `20.19.0` or newer, or Node `22.12.0` or newer. A current LTS version is recommended.

## Get the Project

Choose one option.

### Clone with Git

Copy the HTTPS address from **Code** on the GitHub repository page, then run:

```bash
git clone https://github.com/<owner>/<repository>.git
cd <repository>
npm install
```

Replace `<owner>` and `<repository>` with the values from the GitHub address.

### Download a ZIP File

1. Select **Code > Download ZIP** on GitHub.
2. Extract the ZIP file.
3. Open the extracted folder in VS Code.
4. Select **Terminal > New Terminal**.
5. Run `npm install`.

Do not upload or edit the generated `node_modules/` folder.

## Make the Portfolio Yours

The browser is only a preview. Save changes in the project files, mainly under `src/data/`.

Start with these files:

| What you want to change                                   | File                         |
| --------------------------------------------------------- | ---------------------------- |
| Name, headline, location, email, resume, and social links | `src/data/profile.ts`        |
| About text                                                | `src/data/about.ts`          |
| Section headings and introductions                        | `src/data/sectionContent.ts` |
| Schools and qualifications                                | `src/data/education.ts`      |
| Work, internships, mentoring, or volunteering             | `src/data/experience.ts`     |
| Awards and recognition                                    | `src/data/awards.ts`         |
| Projects, project images, links, and tools                | `src/data/projects.ts`       |
| Gallery photos                                            | `src/data/gallery.ts`        |
| Videos                                                    | `src/data/videos.ts`         |
| Skills                                                    | `src/data/skills.ts`         |
| Certificates                                              | `src/data/certificates.ts`   |
| External blog links                                       | `src/data/blog.ts`           |
| Journal post details                                      | `src/data/journalPosts.ts`   |
| Section order and visibility                              | `src/data/navigation.ts`     |
| Initial portfolio style                                   | `src/data/template.ts`       |

Save a file and check the browser preview. If the preview is not running, use:

```bash
npm run dev
```

### Choose a Portfolio Style

Visitors can currently switch between two styles using the **Portfolio style** button:

- **Engineering**: technical presentation with fixed navigation.
- **Business**: polished editorial casebook.

Both visible styles use the same profile, education, experience, awards, projects, gallery, writing, skills, and contact content. You do not maintain separate copies of your information for Business.

To choose the style shown to a first-time visitor, edit `src/data/template.ts`:

```ts
export const selectedTemplateId = "engineering";
```

Use `"engineering"` or `"business"` for the visitor experience.

A visitor's saved choice overrides this initial value. To test the initial value again, clear the site's browser data or run this in the browser console:

```js
localStorage.removeItem("portfolio-template-id");
location.reload();
```

Older copies of the site may have saved the removed Neutral style. That old choice now opens Engineering automatically.

### Add Images, a Resume, or Certificates

- Put images and logos in `src/assets/`.
- Put project covers in `src/assets/projects/`.
- Put the resume in `src/assets/documents/`.
- Put certificate PDFs in `src/assets/certificates/`.

If you use a new filename, update the import in the matching `src/data/` file. Describe what an image shows in its `imageAlt` text so screen-reader users receive useful information.

### Add Writing

For a post that opens inside the portfolio:

1. Add a Markdown file under `src/content/journal/`.
2. Add its title, date, summary, topics, and content import to `src/data/journalPosts.ts`.

For a post hosted elsewhere, add the link and details to `src/data/blog.ts`.

## Verify Your Changes

Check both visible styles in light and dark mode. Also try a narrow browser window and verify that navigation, images, links, resume downloads, and journal posts work.

Then run:

```bash
npm test
npm run lint
npm run build
```

For a final check of the production version:

```bash
npm run preview
```

Open the printed address, inspect the site, then press `Ctrl+C`.

## Publish with GitHub Pages

The project already includes a GitHub Pages workflow.

1. Push the project to GitHub.
2. Open **Settings > Pages** in the repository.
3. Set **Source** to **GitHub Actions**.
4. Push changes to the `main` branch.
5. Check the **Actions** tab, then open the published Pages address.

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed publishing and URL troubleshooting.

## Update an Existing Copy Safely

Back up or commit your edits first. For a cloned repository, run:

```bash
git status
git pull --ff-only
npm install
```

If Git reports a conflict, do not discard your files. Ask a teacher, mentor, or experienced Git user to help combine the changes.

For a ZIP download, extract the newer version into a separate folder and copy your customized `src/data/`, `src/content/`, and `src/assets/` files carefully.

## Common Problems

### A command is not recognized

Close and reopen the terminal. If `git`, `node`, or `npm` is still missing, reinstall that tool. Confirm that Node meets the minimum version listed above.

### `npm install` cannot find `package.json`

Your terminal is in the wrong folder. Move into the folder containing this README and `package.json`, then try again.

### The page does not update

Confirm `npm run dev` is still running, save the file, and verify that your terminal and editor opened the same project folder.

### The initial portfolio style does not appear

The browser may have saved a visitor choice. Clear the site's browser data or remove `portfolio-template-id` from local storage as shown above.

### An image or PDF is missing

Check the filename, capitalization, import, and folder. Run `npm run build` to catch missing files.

### SWC reports `Failed to load native binding`

This usually means `node_modules` was copied from another computer or contains a damaged native file. Keep a recoverable backup and reinstall exactly from the lock file.

macOS or Linux:

```bash
mv node_modules node_modules.corrupt
npm cache verify
npm ci
```

Windows PowerShell:

```powershell
Rename-Item node_modules node_modules.corrupt
npm cache verify
npm ci
```

Confirm the repair:

```bash
node -e "require('@swc/core'); console.log('SWC OK')"
npm run dev
```

After the site works, delete the `node_modules.corrupt` backup.

## For Developers

The site uses React 19, TypeScript, Vite, Chakra UI, Tailwind CSS, Vitest, ESLint, GitHub Actions, and GitHub Pages. Shared presentation components are under `src/components/`; visual templates are under `src/templates/`; shared types are in `src/types/portfolio.ts`.

## License

MIT
