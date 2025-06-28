%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TVMVP
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Time-Varying Minimum Variance Portfolio

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-prettyunits 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-prettyunits 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 

%description
Provides the estimation of a time-dependent covariance matrix of returns
with the intended use for portfolio optimization. The package offers
methods for determining the optimal number of factors to be used in the
covariance estimation, a hypothesis test of time-varying covariance, and
user-friendly functions for portfolio optimization and rolling window
evaluation. The local PCA method, method for determining the number of
factors, and associated hypothesis test are based on Su and Wang (2017)
<doi:10.1016/j.jeconom.2016.12.004>. The approach to time-varying
portfolio optimization follows Fan et al. (2024)
<doi:10.1016/j.jeconom.2022.08.007>. The regularisation applied to the
residual covariance matrix adopts the technique introduced by Chen et al.
(2019) <doi:10.1016/j.jeconom.2019.04.025>.

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
