%global __brp_check_rpaths %{nil}
%global packname  fgdr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Fundamental Geo-Spatial Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-raster >= 2.6.7
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-jpmesh >= 1.1.1
BuildRequires:    R-CRAN-terra >= 0.8.2
BuildRequires:    R-CRAN-units >= 0.6.6
BuildRequires:    R-CRAN-sf >= 0.6.3
BuildRequires:    R-CRAN-stars >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-jpmesh >= 1.1.1
Requires:         R-CRAN-terra >= 0.8.2
Requires:         R-CRAN-units >= 0.6.6
Requires:         R-CRAN-sf >= 0.6.3
Requires:         R-CRAN-stars >= 0.3.1
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-rlang >= 0.2.2

%description
Read and Parse for Fundamental Geo-Spatial Data (FGD) which downloads XML
file from providing site (<https://fgd.gsi.go.jp/download/menu.php>). The
JPGIS format file provided by FGD so that it can be handled as an R
spatial object such as 'sf' and 'raster', 'terra' or 'stars'. Supports the
FGD version 4.1, and accepts fundamental items and digital elevation
models.

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
