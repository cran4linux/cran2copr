%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dr
%global packver   3.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Dimension Reduction for Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-graphics 

%description
Functions, methods, and datasets for fitting dimension reduction
regression, using slicing (methods SAVE and SIR), Principal Hessian
Directions (phd, using residuals and the response), and an iterative IRE.
Partial methods, that condition on categorical predictors are also
available.  A variety of tests, and stepwise deletion of predictors, is
also included.  Also included is code for computing permutation tests of
dimension.  Adding additional methods of estimating dimension is
straightforward. For documentation, see the vignette in the package.  With
version 3.0.4, the arguments for dr.step have been modified.

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
