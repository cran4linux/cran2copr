%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TSQLEM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Two Stage Estimation for Generalized Structural Equation Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.6.0
Requires:         R-core >= 4.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 

%description
Provides a framework to estimate high dimensional generalized structural
equation models using two stage quasi-likelihood expectation-maximization.
The structural model supports binomial (logit and probit), Poisson,
negative binomial, and gamma distributions for the outcome variable.
Hattab (2026) "A Two Stage Quasi-Likelihood Estimation Method for High
Dimensional Generalized Structural Equation Models"
<doi:10.48550/arXiv.2608.16017>.

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
