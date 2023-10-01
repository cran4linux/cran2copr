%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DynareR
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bringing the Power of 'Dynare' to 'R', 'R Markdown', and 'Quarto'

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-magrittr 

%description
It allows running 'Dynare' program from base R, R Markdown and Quarto.
'Dynare' is a software platform for handling a wide class of economic
models, in particular dynamic stochastic general equilibrium ('DSGE') and
overlapping generations ('OLG') models.  This package does not only
integrate R and Dynare but also serves as a 'Dynare' Knit-Engine for
'knitr' package. The package requires 'Dynare' (<https://www.dynare.org/>)
and 'Octave' (<https://www.octave.org/download.html>).  Write all your
'Dynare' commands in R or R Markdown chunk.

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
