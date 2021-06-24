%global __brp_check_rpaths %{nil}
%global packname  MIIPW
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          IPW and Mean Score Methods for Time-Course Missing Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-matlib 
BuildRequires:    R-stats 
Requires:         R-CRAN-R2jags 
Requires:         R-utils 
Requires:         R-CRAN-matlib 
Requires:         R-stats 

%description
Contains functions for data analysis of Repeated measurement
continuous,categorical data using MCMC. Data may contain missing value in
response and covariates. Mean Score Method and Inverse Probability
Weighted method for parameter estimation when there is missing value in
covariates are also included. Reference for mean score method, inverse
probability weighted method is Wang et
al(2007)<doi:10.1093/biostatistics/kxl024>.

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
