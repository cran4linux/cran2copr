%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bridgr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bridging Data Frequencies for Timely Economic Forecasts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-tsbox 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-forecast 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-tsbox 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-forecast 

%description
Implements bridge models for nowcasting and forecasting macroeconomic
variables by linking high-frequency indicator variables (e.g., monthly
data) to low-frequency target variables (e.g., quarterly GDP). Simplifies
forecasting and aggregating indicator variables to match the target
frequency, enabling timely predictions ahead of official data releases.
For more on bridge models, see Baffigi, A., Golinelli, R., & Parigi, G.
(2004) <doi:10.1016/S0169-2070(03)00067-0>, Burri (2023)
<https://www5.unine.ch/RePEc/ftp/irn/pdfs/WP23-02.pdf> or Schumacher
(2016) <doi:10.1016/j.ijforecast.2015.07.004>.

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
