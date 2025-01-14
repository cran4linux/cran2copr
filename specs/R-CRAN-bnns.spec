%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bnns
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Neural Network with 'Stan'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-rstan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-BH 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-rstan 
Requires:         R-stats 
Requires:         R-CRAN-rstantools

%description
Offers a flexible formula-based interface for building and training
Bayesian Neural Networks powered by 'Stan'. The package supports modeling
complex relationships while providing rigorous uncertainty quantification
via posterior distributions. With features like user chosen priors, clear
predictions, and support for regression, binary, and multi-class
classification, it is well-suited for applications in clinical trials,
finance, and other fields requiring robust Bayesian inference and
decision-making. References: Neal(1996) <doi:10.1007/978-1-4612-0745-0>.

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
