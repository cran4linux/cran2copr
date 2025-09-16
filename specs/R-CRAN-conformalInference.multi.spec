%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  conformalInference.multi
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Conformal Inference Tools for Regression with Multivariate Response

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-future.apply >= 1.8.1
BuildRequires:    R-CRAN-future >= 1.23.0
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-future.apply >= 1.8.1
Requires:         R-CRAN-future >= 1.23.0
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-utils 

%description
It computes full conformal, split conformal and multi-split conformal
prediction regions when the response variable is multivariate (i.e.
dimension is greater than one). Moreover, the package also contains plot
functions to visualize the output of the full and split conformal
functions. To guarantee consistency, the package structure mimics the
univariate package 'conformalInference' by Ryan Tibshirani. See Lei,
G’sell, Rinaldo, Tibshirani, & Wasserman (2018)
<doi:10.1080/01621459.2017.1307116> for full and split conformal
prediction in regression, and Barber, Candès, Ramdas, & Tibshirani (2023)
<doi:10.1214/23-AOS2276> for extensions beyond exchangeability.

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
