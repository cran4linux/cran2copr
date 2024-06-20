%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dbnR
%global packver   0.7.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.9
Release:          1%{?dist}%{?buildtag}
Summary:          Dynamic Bayesian Network Learning and Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-MASS >= 7.3.55
BuildRequires:    R-CRAN-bnlearn >= 4.5
BuildRequires:    R-stats >= 3.6.0
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-MASS >= 7.3.55
Requires:         R-CRAN-bnlearn >= 4.5
Requires:         R-stats >= 3.6.0
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-Rcpp >= 1.0.2

%description
Learning and inference over dynamic Bayesian networks of arbitrary
Markovian order. Extends some of the functionality offered by the
'bnlearn' package to learn the networks from data and perform exact
inference. It offers three structure learning algorithms for dynamic
Bayesian networks: Trabelsi G. (2013) <doi:10.1007/978-3-642-41398-8_34>,
Santos F.P. and Maciel C.D. (2014) <doi:10.1109/BRC.2014.6880957>, Quesada
D., Bielza C. and Larrañaga P. (2021) <doi:10.1007/978-3-030-86271-8_14>.
It also offers the possibility to perform forecasts of arbitrary length. A
tool for visualizing the structure of the net is also provided via the
'visNetwork' package.

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
