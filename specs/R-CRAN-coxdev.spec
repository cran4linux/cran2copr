%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coxdev
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cox Model Deviance, Gradient, Information and Score Sampling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Fast computation of the deviance of the Cox proportional hazards model
(Cox (1972) <doi:10.1111/j.2517-6161.1972.tb00899.x>), its gradient and
the diagonal of its Hessian with respect to the linear predictor, the
information and its derivative in a direction as matrix-free linear
operators, and draws of the score (multinomial, Bernoulli, Fisher
noncentral hypergeometric or wild), with the ties of Breslow (1974)
<doi:10.2307/2529620> or Efron (1977)
<doi:10.1080/01621459.1977.10480613>, start times (left truncation),
strata and sample weights. The 'C++' code is header-only, shared with the
'Python' package 'coxdev', and installed for packages that use it through
'LinkingTo'.

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
