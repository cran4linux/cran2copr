%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SeaVal
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Validation of Seasonal Weather Forecasts

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggplotify 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggplotify 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-scales 

%description
Provides tools for processing and evaluating seasonal weather forecasts,
with an emphasis on tercile forecasts. We follow the World Meteorological
Organization's "Guidance on Verification of Operational Seasonal Climate
Forecasts", S.J.Mason (2018, ISBN: 978-92-63-11220-0, URL:
<https://library.wmo.int/idurl/4/56227>). The development was supported by
the European Union’s Horizon 2020 research and innovation programme under
grant agreement no. 869730 (CONFER). A comprehensive online tutorial is
available at <http://files.nr.no/samba/CONFER/SeaVal/>.

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
