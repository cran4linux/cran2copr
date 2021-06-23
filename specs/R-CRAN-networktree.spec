%global __brp_check_rpaths %{nil}
%global packname  networktree
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Recursive Partitioning of Network Models

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-grid 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-qgraph 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Formula 
Requires:         R-grid 
Requires:         R-graphics 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-reshape2 

%description
Network trees recursively partition the data with respect to covariates.
Two network tree algorithms are available: model-based trees based on a
multivariate normal model and nonparametric trees based on covariance
structures. After partitioning, correlation-based networks (psychometric
networks) can be fit on the partitioned data. For details see Jones, Mair,
Simon, & Zeileis (2020) <doi:10.1007/s11336-020-09731-4>.

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
