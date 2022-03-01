%global __brp_check_rpaths %{nil}
%global packname  thunder
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Computation and Visualisation of Atmospheric Convective Parameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.9.4
BuildRequires:    R-CRAN-climate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-aiRthermo 
Requires:         R-CRAN-Rcpp >= 0.12.9.4
Requires:         R-CRAN-climate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-aiRthermo 

%description
Collection of functions for rapid computation and visualisation of
convective parameters commonly used in the operational prediction of
severe convective storms. Core algorithm is based on a highly optimized
'C++' code linked into 'R' via 'Rcpp'. Highly efficient engine allows to
derive thermodynamic and kinematic parameters from large numerical
datasets such as reanalyses or operational Numerical Weather Prediction
models in a reasonable amount of time. Package has been developed since
2017 by research meteorologists specializing in severe thunderstorms.

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
