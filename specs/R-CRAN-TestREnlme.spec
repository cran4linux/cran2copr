%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TestREnlme
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Tests for Random Effects in Linear and Nonlinear Mixed-Effects Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.54
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-nlme >= 3.1.150
BuildRequires:    R-CRAN-withr >= 3.0.2
BuildRequires:    R-CRAN-nls.multstart >= 2.0.0
BuildRequires:    R-CRAN-mgsub >= 1.7.3
BuildRequires:    R-CRAN-Matrix >= 1.3.0
BuildRequires:    R-CRAN-matrixcalc >= 1.0.5
BuildRequires:    R-CRAN-expm >= 0.999.6
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-MASS >= 7.3.54
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-nlme >= 3.1.150
Requires:         R-CRAN-withr >= 3.0.2
Requires:         R-CRAN-nls.multstart >= 2.0.0
Requires:         R-CRAN-mgsub >= 1.7.3
Requires:         R-CRAN-Matrix >= 1.3.0
Requires:         R-CRAN-matrixcalc >= 1.0.5
Requires:         R-CRAN-expm >= 0.999.6
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
Provides nonparametric permutation tests for testing all or any subset of
random effects in linear and nonlinear mixed-effects models, without
requiring normality or other distributional assumptions on random effects
or errors. Three distribution-free variance-component estimators are
implemented: Variance Least Squares ('VLS'), Method of Moments ('MM'), and
Method of Moments with First-Order Approximation ('MMF'). A permutation
procedure is used to obtain finite-sample p-values. Plotting functions
support data exploration, model evaluation, and communication of results.
Methods are described in Uwimpuhwe, Drikvandi, and Blozis (2026)
<doi:10.1002/sim.70605>.

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
