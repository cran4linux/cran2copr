%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROBOSRMSMOTE
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Oversampling with RM-SMOTE for Imbalanced Classification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rrcov >= 1.7.0
BuildRequires:    R-CRAN-meanShiftR >= 0.56
BuildRequires:    R-stats 
Requires:         R-CRAN-rrcov >= 1.7.0
Requires:         R-CRAN-meanShiftR >= 0.56
Requires:         R-stats 

%description
Provides the ROBOSRMSMOTE (Robust Oversampling with RM-SMOTE) framework
for imbalanced classification tasks. This package extends Mahalanobis
distance-based oversampling techniques by integrating robust covariance
estimators to better handle outliers and complex data distributions. The
implemented methodology builds upon and significantly expands the RM-SMOTE
algorithm originally proposed by Taban et al. (2025)
<doi:10.1007/s10260-025-00819-8>.

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
