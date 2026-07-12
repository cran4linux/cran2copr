%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Romeb
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Median-Based Bayesian Growth Curve Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-rjags 
Requires:         R-stats 
Requires:         R-utils 

%description
Implements robust median-based Bayesian linear growth curve models for
complete data and for data with Missing Completely at Random (MCAR),
Missing At Random (MAR), or Missing Not At Random (MNAR) mechanisms.
Models are fitted using 'rjags' through 'JAGS' and posterior summaries are
computed with 'coda'. The main function allows users to specify outcome
variables, auxiliary variables for MNAR missingness models, prior
hyperparameters, and initial values directly through function arguments.

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
