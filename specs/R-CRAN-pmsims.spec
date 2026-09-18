%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pmsims
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Sample Size Tools for Prediction Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-mlpwr 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-timeROC 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-mlpwr 
Requires:         R-CRAN-pROC 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-timeROC 
Requires:         R-utils 

%description
Provides a flexible, simulation-based toolkit for exploring how much data
are needed to develop reliable prediction models. It works by repeatedly
generating data, fitting models, and evaluating performance to show how
sample size affects predictive accuracy, calibration, and overfitting. The
package supports continuous, binary, and time-to-event outcomes and can be
used with both regression-based modelling approaches and machine-learning
methods. It is designed to help researchers plan studies, assess
feasibility, and build more robust and generalisable models. The methods
are described in Olaniran et al. (2026) <doi:10.1186/s12874-026-02935-9>
and Shamsutdinova et al. (2026) <doi:10.48550/arXiv.2602.23507>.

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
