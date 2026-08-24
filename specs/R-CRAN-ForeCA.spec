%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ForeCA
%global packver   0.2.8-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Forecastable Component Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-astsa >= 1.10
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-astsa >= 1.10
Requires:         R-CRAN-MASS 
Requires:         R-graphics 
Requires:         R-utils 

%description
Implementation of Forecastable Component Analysis ('ForeCA'), including
main algorithms and auxiliary function (summary, plotting, etc.) to apply
'ForeCA' to multivariate time series data. 'ForeCA' is a novel dimension
reduction (DR) technique for temporally dependent signals. Contrary to
other popular DR methods, such as 'PCA' or 'ICA', 'ForeCA' takes time
dependency explicitly into account and searches for the most
''forecastable'' signal. The measure of forecastability is based on the
Shannon entropy of the spectral density of the transformed signal.

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
