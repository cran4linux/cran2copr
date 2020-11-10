%global packname  BayesMassBal
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Data Reconciliation of Separation Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-HDInterval 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-HDInterval 
Requires:         R-CRAN-coda 

%description
Bayesian tools that can be used to reconcile, or mass balance, mass flow
rate data collected from chemical or particulate separation processes
aided by constraints governed by the conservation of mass. Functions
included in the package aid the user in organizing and constraining data,
using Markov chain Monte Carlo methods to obtain samples from Bayesian
models, and in computation of the marginal likelihood of the data, given a
particular model, for model selection.  Marginal likelihood is
approximated by methods in Chib S (1995) <doi:10.2307/2291521>.

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
