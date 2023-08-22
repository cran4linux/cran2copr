%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LTAR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tensor Forecasting Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-rTensor2 
BuildRequires:    R-CRAN-gsignal 
Requires:         R-CRAN-vars 
Requires:         R-stats 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-rTensor2 
Requires:         R-CRAN-gsignal 

%description
A set of tools for forecasting the next step in a multidimensional setting
using tensors.  In the examples, a forecast is made of sea surface
temperatures of a geographic grid (i.e. lat/long).  Each observation is a
matrix, the entries in the matrix and the sea surface temperature at a
particular lattitude/longitude. Cates, J., Hoover, R. C., Caudle, K.,
Kopp, R., & Ozdemir, C. (2021) "Transform-Based Tensor Auto Regression for
Multilinear Time Series Forecasting" in 2021 20th IEEE International
Conference on Machine Learning and Applications (ICMLA) (pp. 461-466),
IEEE <doi:10.1109/ICMLA52953.2021.00078>.

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
