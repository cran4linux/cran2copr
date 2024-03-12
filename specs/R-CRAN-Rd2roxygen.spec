%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rd2roxygen
%global packver   1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15
Release:          1%{?dist}%{?buildtag}
Summary:          Convert Rd to 'Roxygen' Documentation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-roxygen2 >= 4.0.0
BuildRequires:    R-CRAN-formatR >= 1.0
BuildRequires:    R-CRAN-xfun >= 0.13
Requires:         R-CRAN-roxygen2 >= 4.0.0
Requires:         R-CRAN-formatR >= 1.0
Requires:         R-CRAN-xfun >= 0.13

%description
Functions to convert Rd to 'roxygen' documentation. It can parse an Rd
file to a list, create the 'roxygen' documentation and update the original
R script (e.g. the one containing the definition of the function)
accordingly. This package also provides utilities that can help developers
build packages using 'roxygen' more easily. The 'formatR' package can be
used to reformat the R code in the examples sections so that the code will
be more readable.

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
