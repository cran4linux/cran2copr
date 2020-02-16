%global packname  forestChange
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Computing Essential Biodiversity Variables from Global ForestChange Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-landscapemetrics 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-parallel 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-rvest 
Requires:         R-stats 
Requires:         R-CRAN-landscapemetrics 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-dplyr 

%description
Metrics and statistics of Essential Biodiversity Variables are computed by
processing Global Forest Change data (Hansen et al., 2013)
<doi:10.1126/science.1244693> , Canopy Cover data (Sexton et al., 2013)
<doi:10.1080/17538947.2013.786146>, and polygon geometries (e.g., GADM,
see <https://gadm.org/>).

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
