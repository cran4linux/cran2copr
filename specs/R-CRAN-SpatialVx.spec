%global __brp_check_rpaths %{nil}
%global packname  SpatialVx
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Forecast Verification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 6.8
BuildRequires:    R-CRAN-spatstat >= 2.0.0
BuildRequires:    R-CRAN-smoothie 
BuildRequires:    R-CRAN-smatr 
BuildRequires:    R-CRAN-turboEM 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-spatstat.core 
BuildRequires:    R-CRAN-spatstat.linnet 
BuildRequires:    R-CRAN-distillery 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-waveslim 
Requires:         R-CRAN-fields >= 6.8
Requires:         R-CRAN-spatstat >= 2.0.0
Requires:         R-CRAN-smoothie 
Requires:         R-CRAN-smatr 
Requires:         R-CRAN-turboEM 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-spatstat.core 
Requires:         R-CRAN-spatstat.linnet 
Requires:         R-CRAN-distillery 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-waveslim 

%description
Spatial forecast verification refers to verifying weather forecasts when
the verification set (forecast and observations) is on a spatial field,
usually a high-resolution gridded spatial field.  Most of the functions
here require the forecast and observed fields to be gridded and on the
same grid.  For a thorough review of most of the methods in this package,
please see Gilleland et al. (2009) <doi: 10.1175/2009WAF2222269.1>.

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
