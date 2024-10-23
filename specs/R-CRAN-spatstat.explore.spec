%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatstat.explore
%global packver   3.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Data Analysis for the 'spatstat' Family

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat.geom >= 3.3.2
BuildRequires:    R-CRAN-spatstat.random >= 3.3.1
BuildRequires:    R-CRAN-spatstat.data >= 3.1.2
BuildRequires:    R-CRAN-spatstat.utils >= 3.1.0
BuildRequires:    R-CRAN-spatstat.sparse >= 3.1.0
BuildRequires:    R-CRAN-spatstat.univar >= 3.0.0
BuildRequires:    R-CRAN-goftest >= 1.2.2
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-spatstat.geom >= 3.3.2
Requires:         R-CRAN-spatstat.random >= 3.3.1
Requires:         R-CRAN-spatstat.data >= 3.1.2
Requires:         R-CRAN-spatstat.utils >= 3.1.0
Requires:         R-CRAN-spatstat.sparse >= 3.1.0
Requires:         R-CRAN-spatstat.univar >= 3.0.0
Requires:         R-CRAN-goftest >= 1.2.2
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-abind 

%description
Functionality for exploratory data analysis and nonparametric analysis of
spatial data, mainly spatial point patterns, in the 'spatstat' family of
packages. (Excludes analysis of spatial data on a linear network, which is
covered by the separate package 'spatstat.linnet'.) Methods include
quadrat counts, K-functions and their simulation envelopes, nearest
neighbour distance and empty space statistics, Fry plots, pair correlation
function, kernel smoothed intensity, relative risk estimation with
cross-validated bandwidth selection, mark correlation functions,
segregation indices, mark dependence diagnostics, and kernel estimates of
covariate effects. Formal hypothesis tests of random pattern (chi-squared,
Kolmogorov-Smirnov, Monte Carlo, Diggle-Cressie-Loosmore-Ford, Dao-Genton,
two-stage Monte Carlo) and tests for covariate effects
(Cox-Berman-Waller-Lawson, Kolmogorov-Smirnov, ANOVA) are also supported.

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
