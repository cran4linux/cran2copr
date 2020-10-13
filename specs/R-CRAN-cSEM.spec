%global packname  cSEM
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Composite-Based Structural Equation Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-expm >= 0.999.5
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-symmoments 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-expm >= 0.999.5
Requires:         R-CRAN-abind 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-symmoments 
Requires:         R-utils 
Requires:         R-CRAN-lifecycle 

%description
Estimate, assess, test, and study linear, nonlinear, hierarchical and
multigroup structural equation models using composite-based approaches and
procedures, including estimation techniques such as partial least squares
path modeling (PLS-PM) and its derivatives (PLSc, ordPLSc, robustPLSc),
generalized structured component analysis (GSCA), generalized structured
component analysis with uniqueness terms (GSCAm), generalized canonical
correlation analysis (GCCA), principal component analysis (PCA), factor
score regression (FSR) using sum score, regression or bartlett scores
(including bias correction using Croon’s approach), as well as several
tests and typical postestimation procedures (e.g., verify admissibility of
the estimates, assess the model fit, test the model fit etc.).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
