%global packname  himach
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          High Mach Finds Routes for Supersonic Aircraft

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.9.7
BuildRequires:    R-CRAN-cppRouting 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-s2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-sf >= 0.9.7
Requires:         R-CRAN-cppRouting 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-s2 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tidyr 

%description
For supersonic aircraft, flying subsonic over land, High Mach finds the
best route between airports. Allows for coastal buffer and potentially
closed regions. Uses a minimal model of aircraft performance: the focus is
on time saved versus subsonic flight, rather than on vertical flight
profile. For modelling and forecasting, not for planning your flight!

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
