%global packname  dnr
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Dynamic Networks using Exponential Random Graph Models (ERGM) Family

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-ergm 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-network 
Requires:         R-CRAN-ergm 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-glmnet 

%description
Functions are provided to fit temporal lag models to dynamic networks. The
models are build on top of exponential random graph models (ERGM)
framework. There are functions for simulating or forecasting networks for
future time points. Abhirup Mallik & Zack W. Almquist (2019) Stable
Multiple Time Step Simulation/Prediction From Lagged Dynamic Network
Regression Models, Journal of Computational and Graphical Statistics,
28:4, 967-979, <DOI: 10.1080/10618600.2019.1594834>.

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
