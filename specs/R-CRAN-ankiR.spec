%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ankiR
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read and Analyze 'Anki' Flashcard Databases

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 

%description
Comprehensive toolkit for reading and analyzing 'Anki' flashcard
collection databases. Provides functions to access notes, cards, decks,
note types, and review logs with a tidy interface. Features extensive
analytics including retention rates, learning curves, forgetting curve
fitting, and review patterns. Supports 'FSRS' (Free Spaced Repetition
Scheduler) analysis with stability, difficulty, retrievability metrics,
parameter comparison, and workload predictions. Includes visualization
functions, comparative analysis, time-based analytics, card quality
assessment, sibling card analysis, interference detection, predictive
features, session simulation, and an interactive Shiny dashboard.
Academic/exam preparation tools for medical students and board exam
preparation. Export capabilities include CSV, Org-mode, Markdown,
SuperMemo, Mochi, Obsidian SR, and JSON formats with progress reports.

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
