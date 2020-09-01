%global packname  starsExtra
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Functions for Working with 'stars' Rasters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-stars 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-nngeo 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-stars 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-mgcv 
Requires:         R-CRAN-nngeo 
Requires:         R-CRAN-units 

%description
Miscellaneous functions for working with 'stars' objects, mainly
single-band rasters. Currently includes functions for: (1) focal
filtering, (2) detrending of Digital Elevation Models, (3) calculating
flow length, (4) calculating the Convergence Index, (5) calculating
topographic aspect and topographic slope.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
