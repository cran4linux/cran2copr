%global __brp_check_rpaths %{nil}
%global packname  clusterPower
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Power Calculations for Cluster-Randomized and Cluster-Randomized Crossover Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods >= 4.0.0
BuildRequires:    R-CRAN-lmerTest >= 3.1.2
BuildRequires:    R-CRAN-nlme >= 3.1.149
BuildRequires:    R-CRAN-car >= 3.0.4
BuildRequires:    R-CRAN-R.utils >= 2.10.1
BuildRequires:    R-CRAN-foreach >= 1.5.0
BuildRequires:    R-CRAN-progress >= 1.1.2
BuildRequires:    R-CRAN-shiny >= 1.0.5
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-methods >= 4.0.0
Requires:         R-CRAN-lmerTest >= 3.1.2
Requires:         R-CRAN-nlme >= 3.1.149
Requires:         R-CRAN-car >= 3.0.4
Requires:         R-CRAN-R.utils >= 2.10.1
Requires:         R-CRAN-foreach >= 1.5.0
Requires:         R-CRAN-progress >= 1.1.2
Requires:         R-CRAN-shiny >= 1.0.5
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-CRAN-mathjaxr 

%description
Calculate power for cluster randomized trials (CRTs) including multi-arm
trials, individually randomized group treatment trials (IGRTTs), stepped
wedge trials (SWTs) and others using closed-form (analytic) solutions, and
estimates power using Monte Carlo methods.

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
