%global __brp_check_rpaths %{nil}
%global packname  monomvn
%global packver   1.9-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.15
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation for MVN and Student-t Data with Monotone Missingness

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-mvtnorm 

%description
Estimation of multivariate normal (MVN) and student-t data of arbitrary
dimension where the pattern of missing data is monotone. See Pantaleo and
Gramacy (2010) <arXiv:0907.2135>. Through the use of
parsimonious/shrinkage regressions (plsr, pcr, lasso, ridge, etc.), where
standard regressions fail, the package can handle a nearly arbitrary
amount of missing data. The current version supports maximum likelihood
inference and a full Bayesian approach employing scale-mixtures for Gibbs
sampling. Monotone data augmentation extends this Bayesian approach to
arbitrary missingness patterns.  A fully functional standalone interface
to the Bayesian lasso (from Park & Casella), Normal-Gamma (from Griffin &
Brown), Horseshoe (from Carvalho, Polson, & Scott), and ridge regression
with model selection via Reversible Jump, and student-t errors (from
Geweke) is also provided.

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
