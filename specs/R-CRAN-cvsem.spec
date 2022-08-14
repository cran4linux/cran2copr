%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cvsem
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          SEM Model Comparison with K-Fold Cross-Validation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-lavaan 
Requires:         R-stats 
Requires:         R-CRAN-Rdpack 

%description
The goal of 'cvsem' is to provide functions that allow for comparing
Structural Equation Models (SEM) using cross-validation. Users can specify
multiple SEMs using 'lavaan' syntax. 'cvsem' computes the Kullback Leibler
(KL) Divergence between 1) the model implied covariance matrix estimated
from the training data and 2) the sample covariance matrix estimated from
the test data described in Cudeck, Robert & Browne (1983)
<doi:10.18637/jss.v048.i02>. The KL Divergence is computed for each of the
specified SEMs allowing for the models to be compared based on their
prediction errors.

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
