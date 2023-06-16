%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mvDFA
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Detrended Fluctuation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-longmemo 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-RobPer 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-longmemo 
Requires:         R-stats 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-RobPer 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pracma 

%description
This R package provides an implementation of multivariate extensions of a
well-known fractal analysis technique, Detrended Fluctuations Analysis
(DFA; Peng et al., 1995<doi:10.1063/1.166141>), for multivariate time
series: multivariate DFA (mvDFA). Several coefficients are implemented
that take into account the correlation structure of the multivariate time
series to varying degrees. These coefficients may be used to analyze long
memory and changes in the dynamic structure that would by univariate DFA.
Therefore, this R package aims to extend and complement the original
univariate DFA (Peng et al., 1995) for estimating the scaling properties
of nonstationary time series.

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
