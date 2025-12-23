%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  citsr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Controlled Interrupted Time Series Analysis and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-clubSandwich 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-AICcmodavg 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-clubSandwich 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-AICcmodavg 

%description
Implements controlled interrupted time series (CITS) analysis for
evaluating interventions in comparative time-series data. The package
provides tools for preparing panel time-series datasets, fitting models
using generalized least squares (GLS) with optional
autoregressive–moving-average (ARMA) error structures, and computing
fitted values and robust standard errors using cluster-robust variance
estimators (CR2). Visualization functions enable clear presentation of
estimated effects and counterfactual trajectories following interventions.
Background on methods for causal inference in interrupted time series can
be found in Linden and Adams (2011) <doi:10.1111/j.1365-2753.2010.01504.x>
and Lopez Bernal, Cummins, and Gasparrini (2018) <doi:10.1093/ije/dyy135>.

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
