%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pbox
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Exploring Multivariate Spaces with Probability Boxes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-gamlss 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Advanced statistical library offering a method to encapsulate and query
the probability space of a dataset effortlessly using Probability Boxes
(p-boxes). Its distinctive feature lies in the ease with which users can
navigate and analyze marginal, joint, and conditional probabilities while
taking into account the underlying correlation structure inherent in the
data using copula theory and models. A comprehensive explanation is
available in the paper "pbox: Exploring Multivariate Spaces with
Probability Boxes" to be published in the Journal of Statistical Software.

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
