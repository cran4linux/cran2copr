%global packname  fgdr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
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
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-jpmesh >= 1.1.1
BuildRequires:    R-CRAN-sf >= 0.6.3
BuildRequires:    R-CRAN-stars >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-rlang >= 0.2.2
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-raster >= 2.6.7
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-jpmesh >= 1.1.1
Requires:         R-CRAN-sf >= 0.6.3
Requires:         R-CRAN-stars >= 0.3.1
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-rlang >= 0.2.2

%description
Read and Parse for Fundamental Geo-Spatial Data (FGD) which downloads XML
file from providing site (<https://fgd.gsi.go.jp/download/menu.php>). The
JPGIS format file provided by FGD so that it can be handled as an R
spatial object such as 'sf' and 'raster' or 'stars'. Supports the FGD
version 4.1, and accepts fundamental items and digital elevation models.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
