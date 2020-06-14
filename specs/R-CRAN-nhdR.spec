%global packname  nhdR
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          2%{?dist}
Summary:          Tools for working with the National Hydrography Dataset

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         p7zip
BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-foreign 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-units 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-purrr 

%description
Tools for working with the National Hydrography Dataset, with functions
for querying, downloading, and networking both the NHD
<https://www.usgs.gov/core-science-systems/ngp/national-hydrography> and
NHDPlus <https://nhdplus.com/NHDPlus/> datasets.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
