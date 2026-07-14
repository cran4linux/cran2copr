%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  choicer
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Choice Models for Economic Applications

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table 
Requires:         R-graphics 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Fast estimation of discrete-choice models for applied economics.
Frequentist likelihoods, analytical gradients, and Hessians are
implemented in C++ with 'OpenMP' parallelism, scaling efficiently to
specifications with many alternative-specific constants. Compiled Gibbs
samplers provide Bayesian multinomial probit and hierarchical models.
Post-estimation routines cover predicted shares, own- and cross-price
elasticities, diversion ratios, willingness to pay, and welfare
counterfactuals. Supports multinomial logit ('MNL'), mixed logit ('MXL'),
nested logit ('NL'), Bayesian multinomial probit ('MNP'), and hierarchical
Bayesian multinomial logit and probit ('HMNL', 'HMNP').

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
