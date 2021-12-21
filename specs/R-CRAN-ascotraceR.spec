%global __brp_check_rpaths %{nil}
%global packname  ascotraceR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate the Spread of Ascochyta Blight in Chickpea

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.9.2
BuildRequires:    R-CRAN-data.table >= 1.13.0
BuildRequires:    R-CRAN-circular >= 0.4.93
BuildRequires:    R-CRAN-lutz >= 0.3.1
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-lubridate >= 1.7.9.2
Requires:         R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-circular >= 0.4.93
Requires:         R-CRAN-lutz >= 0.3.1
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 

%description
A spatiotemporal model that simulates the spread of Ascochyta blight in
chickpea fields based on location-specific weather conditions. This model
is adapted from a model developed by Diggle et al. (2002)
<doi:10.1094/PHYTO.2002.92.10.1110> for simulating the spread of
anthracnose in a lupin field.

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
