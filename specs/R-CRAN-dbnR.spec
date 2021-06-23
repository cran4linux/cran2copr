%global __brp_check_rpaths %{nil}
%global packname  dbnR
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Bayesian Network Learning and Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-bnlearn >= 4.5
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-bnlearn >= 4.5
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-Rcpp >= 1.0.2

%description
Learning and inference over dynamic Bayesian networks of arbitrary
Markovian order. Extends some of the functionality offered by the
'bnlearn' package to learn the networks from data and perform exact
inference. It offers two structure learning algorithms for dynamic
Bayesian networks and the possibility to perform forecasts of arbitrary
length. A tool for visualizing the structure of the net is also provided
via the 'visNetwork' package.

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
