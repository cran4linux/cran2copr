%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RLumModel
%global packver   0.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Solving Ordinary Differential Equations to Understand Luminescence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-khroma >= 1.8.0
BuildRequires:    R-CRAN-deSolve >= 1.30
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.400.2.0
BuildRequires:    R-CRAN-Luminescence >= 0.9.18
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-khroma >= 1.8.0
Requires:         R-CRAN-deSolve >= 1.30
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-Luminescence >= 0.9.18
Requires:         R-utils 
Requires:         R-methods 

%description
A collection of functions to simulate luminescence signals in quartz and
Al2O3 based on published models.

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
