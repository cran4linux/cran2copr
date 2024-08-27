%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ORTH.Ord
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Alternating Logistic Regression with Orthogonalized Residuals for Correlated Ordinal Outcomes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-MASS 

%description
A modified version of alternating logistic regressions (ALR) with
estimation based on orthogonalized residuals (ORTH) is implemented, which
use paired estimating equations to jointly estimate parameters in marginal
mean and within-association models. The within-cluster association between
ordinal responses is modeled by global pairwise odds ratios (POR). A
finite-sample bias correction is provided to POR parameter estimates based
on matrix multiplicative adjusted orthogonalized residuals (MMORTH) for
correcting estimating equations, and different bias-corrected variance
estimators such as BC1, BC2, and BC3.

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
