%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveydown
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Markdown-Based Surveys Using 'Quarto' and 'shiny'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dotenv 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-RPostgres 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dotenv 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-pool 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-RPostgres 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-usethis 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-yaml 

%description
Generate surveys using markdown and R code chunks. Surveys are composed of
two files: a survey.qmd 'Quarto' file defining the survey content (pages,
questions, etc), and an app.R file defining a 'shiny' app with global
settings (libraries, database configuration, etc.) and server
configuration options (e.g., conditional skipping / display, etc.). Survey
data collected from respondents is stored in a 'PostgreSQL' database.
Features include controls for conditional skip logic (skip to a page based
on an answer to a question), conditional display logic (display a question
based on an answer to a question), a customizable progress bar, and a wide
variety of question types, including multiple choice (single choice and
multiple choices), select, text, numeric, multiple choice buttons, text
area, and dates. Because the surveys render into a 'shiny' app, designers
can also leverage the reactive capabilities of 'shiny' to create dynamic
and interactive surveys.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
