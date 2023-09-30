%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  learnr
%global packver   0.11.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.5
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Tutorials for R

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.31
BuildRequires:    R-CRAN-markdown >= 1.3
BuildRequires:    R-CRAN-rmarkdown >= 1.12
BuildRequires:    R-CRAN-shiny >= 1.0
BuildRequires:    R-CRAN-renv >= 0.8.0
BuildRequires:    R-CRAN-htmltools >= 0.3.5
BuildRequires:    R-CRAN-ellipsis >= 0.2.0.1
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-evaluate 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-promises 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-knitr >= 1.31
Requires:         R-CRAN-markdown >= 1.3
Requires:         R-CRAN-rmarkdown >= 1.12
Requires:         R-CRAN-shiny >= 1.0
Requires:         R-CRAN-renv >= 0.8.0
Requires:         R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-ellipsis >= 0.2.0.1
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-evaluate 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 
Requires:         R-parallel 
Requires:         R-CRAN-promises 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rprojroot 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Create interactive tutorials using R Markdown. Use a combination of
narrative, figures, videos, exercises, and quizzes to create self-paced
tutorials for learning about R and R packages.

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
