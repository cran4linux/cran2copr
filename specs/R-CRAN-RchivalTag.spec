%global __brp_check_rpaths %{nil}
%global packname  RchivalTag
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}%{?buildtag}
Summary:          Analyzing Archival Tagging Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-oceanmap 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-PBSmapping 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-maptools 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-mapdata 
Requires:         R-grDevices 
Requires:         R-CRAN-oceanmap 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-PBSmapping 

%description
A set of functions to generate, access and analyze standard data products
from archival tagging data.

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

%files
%{rlibdir}/%{packname}
