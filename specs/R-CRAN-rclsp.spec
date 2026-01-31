%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rclsp
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Modular Two-Step Convex Optimization Estimator for Ill-Posed Problems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-MASS 

%description
Convex Least Squares Programming (CLSP) is a two-step estimator for
solving underdetermined, ill-posed, or structurally constrained
least-squares problems. It combines pseudoinverse-based estimation with
convex-programming correction methods inspired by Lasso, Ridge, and
Elastic Net to ensure numerical stability, constraint enforcement, and
interpretability. The package also provides numerical stability analysis
and CLSP-specific diagnostics, including partial R^2, normalized RMSE
(NRMSE), Monte Carlo t-tests for mean NRMSE, and condition-number-based
confidence bands.

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
