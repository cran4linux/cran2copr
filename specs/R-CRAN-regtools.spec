%global __brp_check_rpaths %{nil}
%global packname  regtools
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Regression and Classification Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-rje 
BuildRequires:    R-CRAN-text2vec 
BuildRequires:    R-CRAN-polyreg 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-car 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-rje 
Requires:         R-CRAN-text2vec 
Requires:         R-CRAN-polyreg 

%description
Tools for linear, nonlinear and nonparametric regression and
classification.  Novel graphical methods for assessment of parametric
models using nonparametric methods. One vs. All and All vs. All multiclass
classification, optional class probabilities adjustment.  Nonparametric
regression (k-NN) for general dimension, local-linear option.  Nonlinear
regression with Eickert-White method for dealing with heteroscedasticity.
Utilities for converting time series to rectangular form.  Utilities for
conversion between factors and indicator variables.  Some code related to
"Statistical Regression and Classification: from Linear Models to Machine
Learning", N. Matloff, 2017, CRC, ISBN 9781498710916.

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
