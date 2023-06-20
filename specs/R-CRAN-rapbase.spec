%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rapbase
%global packver   1.24.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.24.2
Release:          1%{?dist}%{?buildtag}
Summary:          Base Functions and Resources for Rapporteket

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sship >= 0.9.0
BuildRequires:    R-CRAN-blob 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RMariaDB 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rpivotTable 
BuildRequires:    R-CRAN-sendmailR 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyalert 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-sship >= 0.9.0
Requires:         R-CRAN-blob 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RMariaDB 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rpivotTable 
Requires:         R-CRAN-sendmailR 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyalert 
Requires:         R-utils 
Requires:         R-CRAN-yaml 

%description
Provide common functions and resources for registry specific R-packages at
Rapporteket
<https://rapporteket.github.io/rapporteket/articles/short_introduction.html>.
This package is relevant for developers of packages/registries at
Rapporteket.

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
