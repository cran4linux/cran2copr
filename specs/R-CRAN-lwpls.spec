%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lwpls
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Locally-Weighted Partial Least Squares for 'tidymodels'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-hardhat >= 1.3.0
BuildRequires:    R-CRAN-parsnip >= 1.3.0
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-dials >= 1.2.0
BuildRequires:    R-CRAN-yardstick >= 1.2.0
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-hardhat >= 1.3.0
Requires:         R-CRAN-parsnip >= 1.3.0
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-dials >= 1.2.0
Requires:         R-CRAN-yardstick >= 1.2.0
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-vctrs 

%description
Locally-weighted partial least squares (LW-PLS) is a just-in-time learning
method that builds a dedicated weighted partial least squares model around
every new sample, where training samples are weighted by their similarity
to that sample (Kim et al. (2011) <doi:10.1016/j.ijpharm.2011.10.007>).
Regression (single or multiple outcomes) and classification (locally
weighted partial least squares-discriminant analysis; Bevilacqua and
Marini (2014) <doi:10.1016/j.aca.2014.05.057>) are supported. The local
models can be robust to outliers, by partial robust M-regression (Serneels
et al. (2005) <doi:10.1016/j.chemolab.2005.04.007>), and sparse (Hoffmann
et al. (2015) <doi:10.1016/j.chemolab.2015.09.019>). The prediction kernel
is written in C++ with 'RcppArmadillo', and the model is integrated with
the 'parsnip', 'dials', 'tune' and 'yardstick' packages so it can be used
within the 'tidymodels' framework. Diagnostics of the local models
(prediction reliability, local regression vectors, robust weights and
selected predictors) come with 'ggplot2' plots designed for spectroscopic
data.

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
