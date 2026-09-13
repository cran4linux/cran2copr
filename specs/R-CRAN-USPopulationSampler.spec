%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  USPopulationSampler
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Population-Weighted Sampling of Geographic Locations in the United States

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-curl 
Requires:         R-parallel 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-stats 

%description
Generate geospatial locations within census block groups (BG; the smallest
geographic unit for which population counts are available) within target
counties, states, or across the entirety of the U.S. randomly selected
according to population counts by using the Census Bureau reference data
and optionally allow users to conduct temporal assignments on sampled
locations using Covid-19 data.

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
