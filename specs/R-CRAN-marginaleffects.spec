%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  marginaleffects
%global packver   0.25.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.25.0
Release:          1%{?dist}%{?buildtag}
Summary:          Predictions, Comparisons, Slopes, Marginal Means, and Hypothesis Tests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-data.table >= 1.16.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-insight >= 0.20.3
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-data.table >= 1.16.4
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-insight >= 0.20.3
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-generics 
Requires:         R-methods 
Requires:         R-CRAN-rlang 

%description
Compute and plot predictions, slopes, marginal means, and comparisons
(contrasts, risk ratios, odds, etc.) for over 100 classes of statistical
and machine learning models in R. Conduct linear and non-linear hypothesis
tests, or equivalence tests. Calculate uncertainty estimates using the
delta method, bootstrapping, or simulation-based inference. Details can be
found in Arel-Bundock, Greifer, and Heiss (2024)
<doi:10.18637/jss.v111.i09>.

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
