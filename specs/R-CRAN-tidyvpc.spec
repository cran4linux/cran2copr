%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyvpc
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          VPC Percentiles and Prediction Intervals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantreg >= 5.51
BuildRequires:    R-CRAN-data.table >= 1.9.8
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-utils 
Requires:         R-CRAN-quantreg >= 5.51
Requires:         R-CRAN-data.table >= 1.9.8
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-fastDummies 
Requires:         R-utils 

%description
Perform a Visual Predictive Check (VPC), while accounting for
stratification, censoring, and prediction correction. Using piping from
'magrittr', the intuitive syntax gives users a flexible and powerful
method to generate VPCs using both traditional binning and a new binless
approach Jamsen et al. (2018) <doi:10.1002/psp4.12319> with Additive
Quantile Regression (AQR) and Locally Estimated Scatterplot Smoothing
(LOESS) prediction correction.

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
