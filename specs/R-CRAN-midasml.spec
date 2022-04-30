%global __brp_check_rpaths %{nil}
%global packname  midasml
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Prediction Methods for High-Dimensional Mixed Frequency Time Series Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-snow 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-snow 
Requires:         R-methods 
Requires:         R-CRAN-lubridate 
Requires:         R-stats 

%description
The 'midasml' package implements estimation and prediction methods for
high-dimensional mixed-frequency (MIDAS) time-series and panel data
regression models. The regularized MIDAS models are estimated using
orthogonal (e.g. Legendre) polynomials and sparse-group LASSO (sg-LASSO)
estimator. For more information on the 'midasml' approach see Babii,
Ghysels, and Striaukas (2021, JBES forthcoming)
<doi:10.1080/07350015.2021.1899933>. The package is equipped with the fast
implementation of the sg-LASSO estimator by means of proximal block
coordinate descent. High-dimensional mixed frequency time-series data can
also be easily manipulated with functions provided in the package.

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
