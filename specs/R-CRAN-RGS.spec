%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RGS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Recursive Gradient Scanning Algorithm

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-SemiPar 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-SemiPar 
Requires:         R-CRAN-survival 

%description
Provides a recursive gradient scanning algorithm for discretizing
continuous variables in Logistic and Cox regression models. This algorithm
is especially effective in identifying optimal cut-points for variables
with U-shaped relationships to 'lnOR' (the natural logarithm of the odds
ratio) or 'lnHR' (the natural logarithm of the hazard ratio), thereby
enhancing model fit, interpretability, and predictive power. By
iteratively scanning and calculating gradient changes, the method
accurately pinpoints critical cut-points within nonlinear relationships,
transforming continuous variables into categorical ones. This approach
improves risk classification and regression analysis performance,
increasing interpretability and practical relevance in clinical and risk
management settings.

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
