%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xtune
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Regression with Feature-Specific Penalties Integrating External Information

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-selectiveInference 
BuildRequires:    R-CRAN-lbfgs 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-selectiveInference 
Requires:         R-CRAN-lbfgs 

%description
Extends standard penalized regression (Lasso, Ridge, and Elastic-net) to
allow feature-specific shrinkage based on external information with the
goal of achieving a better prediction accuracy and variable selection.
Examples of external information include the grouping of predictors, prior
knowledge of biological importance, external p-values, function
annotations, etc. The choice of multiple tuning parameters is done using
an Empirical Bayes approach. A majorization-minimization algorithm is
employed for implementation.

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
