%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  webexercises
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Interactive Web Exercises

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-usethis 
Requires:         R-CRAN-rmarkdown >= 2.2
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-yaml 
Requires:         R-grDevices 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-usethis 

%description
Functions for easily creating interactive web exercises in 'R Markdown',
'Quarto', and package vignettes that students can use in self-guided
learning.

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
