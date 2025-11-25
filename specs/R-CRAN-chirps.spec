%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chirps
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          API Client for CHIRPS and CHIRTS

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-terra >= 1.2.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
Requires:         R-CRAN-terra >= 1.2.10
Requires:         R-methods 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-sf 
Requires:         R-stats 

%description
API Client for the Climate Hazards Center 'CHIRPS' and 'CHIRTS'.  The
'CHIRPS' data is a quasi-global (50°S – 50°N) high-resolution (0.05
arc-degrees) rainfall data set, which incorporates satellite imagery and
in-situ station data to create gridded rainfall time series for trend
analysis and seasonal drought monitoring. 'CHIRTS' is a quasi-global (60°S
– 70°N), high-resolution data set of daily maximum and minimum
temperatures. For more details on 'CHIRPS' and 'CHIRTS' data please visit
its official home page <https://www.chc.ucsb.edu/data>.

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
