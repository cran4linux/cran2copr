%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  boiwsa
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Seasonal Adjustment of Weekly Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-MuMIn 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 

%description
Perform seasonal adjustment of weekly data. The package offers a
user-friendly interface for computing seasonally adjusted estimates of
weekly data and also includes diagnostic tools to assess the quality of
the adjustments. Furthermore, it incorporates tools uniquely tailored to
the specific characteristics of Israeli data. The method is described in
more detail in Ginker (2023) <DOI:10.13140/RG.2.2.12221.44000>.

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
