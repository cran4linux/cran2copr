%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nlmeVPC
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Visual Model Checking for Nonlinear Mixed Effect Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-timeDate 

%description
Various visual and numerical diagnosis methods for the nonlinear mixed
effect model, including visual predictive checks, numerical predictive
checks, and coverage plot (Karlsson and Holford, 2008,
<https://www.page-meeting.org/?abstract=1434>).

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
