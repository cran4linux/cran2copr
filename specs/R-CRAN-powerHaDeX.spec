%global __brp_check_rpaths %{nil}
%global packname  powerHaDeX
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Simulation of HDX-MS Data and Tools for the Statistical Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-signal 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-signal 

%description
Facilitates simulating and analyzing data coming from HDX-MS experiments
along with the possibility of comparing the power of the tests verifying
differences in the levels of deuterium uptake. The simulation of mass
spectra is a fast version of <https://github.com/kanzy/HX-MS-Simulations>.

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
