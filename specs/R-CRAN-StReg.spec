%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StReg
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Student's t Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ADGofTest 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-tseries 
Requires:         R-CRAN-ADGofTest 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-tseries 

%description
It contains functions to estimate multivariate Student's t dynamic and
static regression models for given degrees of freedom and lag length.
Users can also specify the trends and dummies of any kind in matrix form.
Poudyal, N., and Spanos, A. (2022) <doi:10.3390/econometrics10020017>.
Spanos, A. (1994) <http://www.jstor.org/stable/3532870>.

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
