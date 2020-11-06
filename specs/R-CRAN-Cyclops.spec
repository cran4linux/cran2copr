%global packname  Cyclops
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cyclic Coordinate Descent for Logistic, Poisson and Survival Analysis

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-BH >= 1.51.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.2
BuildRequires:    R-CRAN-Andromeda >= 0.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-bit64 
Requires:         R-CRAN-Andromeda >= 0.3.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-bit64 

%description
This model fitting tool incorporates cyclic coordinate descent and
majorization-minimization approaches to fit a variety of regression models
found in large-scale observational healthcare data.  Implementations focus
on computational optimization and fine-scale parallelization to yield
efficient inference in massive datasets.  Please see: Suchard, Simpson,
Zorych, Ryan and Madigan (2013) <doi:10.1145/2414416.2414791>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
