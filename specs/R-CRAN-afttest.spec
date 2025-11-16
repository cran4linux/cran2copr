%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  afttest
%global packver   4.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model Diagnostics for Accelerated Failure Time Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-aftgee 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-aftgee 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 

%description
A collection of model checking methods for semiparametric accelerated
failure time (AFT) models under the rank-based approach. For the
(computational) efficiency, Gehan's weight is used. It provides functions
to verify whether the observed data fit the specific model assumptions
such as a functional form of each covariate, a link function, and an
omnibus test. The p-value offered in this package is based on the
Kolmogorov-type supremum test and the variance of the proposed test
statistics is estimated through the re-sampling method. Furthermore, a
graphical technique to compare the shape of the observed residual to a
number of the approximated realizations is provided. See the following
references; A general model-checking procedure for semiparametric
accelerated failure time models, Statistics and Computing, 34 (3), 117
<doi:10.1007/s11222-024-10431-7>; Diagnostics for semiparametric
accelerated failure time models with R package 'afttest', arXiv,
<doi:10.48550/arXiv.2511.09823>.

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
