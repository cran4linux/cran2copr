%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hmcdm
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Hidden Markov Cognitive Diagnosis Models for Learning

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-CRAN-bayesplot >= 1.9.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-rstantools >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-progress 
Requires:         R-stats >= 3.0.0
Requires:         R-CRAN-bayesplot >= 1.9.0
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-rstantools >= 1.0.0

%description
Fitting hidden Markov models of learning under the cognitive diagnosis
framework. The estimation of the hidden Markov diagnostic classification
model, the first order hidden Markov model, the reduced-reparameterized
unified learning model, and the joint learning model for responses and
response times. Chen, Y., Culpepper, S. A., Wang, S., & Douglas, J. (2018)
<doi:10.1177/0146621617721250>. Wang, S., Yang, Y., Culpepper, S. A., &
Douglas, J. A. (2018) <doi:10.3102/1076998617719727>. Wang, S., Zhang, S.,
Douglas, J., & Culpepper, S. (2018) <doi:10.1080/15366367.2018.1435105>.
Zhang, S., Douglas, J. A., Wang, S. & Culpepper, S. A. (2019)
<doi:10.1007/978-3-030-05584-4_24>.

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
