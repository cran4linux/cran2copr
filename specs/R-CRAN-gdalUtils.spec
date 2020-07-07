%global packname  gdalUtils
%global packver   2.0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3.2
Release:          3%{?dist}
Summary:          Wrappers for the Geospatial Data Abstraction Library (GDAL)Utilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         gdal
BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 

%description
Wrappers for the Geospatial Data Abstraction Library (GDAL) Utilities.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/INDEX
