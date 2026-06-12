%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tutorizeR
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Convert R Markdown or Quarto Content into Interactive Tutorials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-yaml 

%description
Helps teachers convert existing '.Rmd' and '.qmd' teaching material into
interactive tutorials for 'learnr' or 'quarto-live'. Conversion preserves
narrative text, setup chunks, and major chunk options, supports teacher
tags, and provides explicit validation and conversion reports. Output
conventions follow 'learnr' as described by Aden-Buie et al. (2025)
<doi:10.32614/CRAN.package.learnr>, 'quarto-live' as described by Stagg
(2024) <https://tidyverse.org/blog/2024/10/quarto-live-0-1-1/>, and R
Markdown as described by Xie, Allaire and Grolemund (2018,
ISBN:9781138359338).

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
