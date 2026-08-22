%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AugBalWeight
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Augmented Balancing Weights as Linear Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Implements augmented balancing weights for causal inference and linear
functional estimation based on David Bruns-Smith, Oliver Dukes, Avi
Feller, and Elizabeth L. Ogburn (2026) <doi:10.1093/jrsssb/qkaf019>.
Establishes numerical equivalence between augmented balancing weight
estimators and single linear models with weighted regression coefficients.
Provides flexible routines for double ridge (l2 balancing), double lasso
(l-infinity balancing), and generalized augmented linear outcome models.
Features cross-validation procedures for tuning outcome penalty
parameters, covariate balance, and Riesz loss. Supports robust
influence-function-based standard errors, bootstrap confidence intervals,
balance diagnostic tools, and counterfactual prediction for treatment
effects such as average treatment effect (ATE) and average treatment
effect on the treated (ATT), expanding upon the doubly robust estimation
framework established by Robins, Rotnitzky, and Zhao (1994)
<doi:10.1080/01621459.1994.10476818> and Chernozhukov, Chetverikov,
Demirer, Duflo, Hansen, Newey, and Robins (2018) <doi:10.1111/ectj.12097>.

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
