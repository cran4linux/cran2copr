%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  savvySh
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Slab and Shrinkage Linear Regression Estimation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-mnormt 
Requires:         R-stats 

%description
Implements a suite of shrinkage estimators for multivariate linear
regression to improve estimation stability and predictive accuracy.
Provides methods including the Stein estimator, Diagonal Shrinkage, the
general Shrinkage estimator (solving a Sylvester equation), and Slab
Regression (Simple and Generalized). These methods address Stein's paradox
by introducing structured bias to reduce variance without requiring
cross-validation, except for Shrinkage Ridge Regression where the
intensity is chosen by minimizing an explicit Mean Squared Error (MSE)
criterion. Methods are based on paper
<https://openaccess.city.ac.uk/id/eprint/35005/>.

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
