%global packname  modiscloud
%global packver   0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14
Release:          3%{?dist}%{?buildtag}
Summary:          R tools for processing Level 2 Cloud Mask products from MODIS

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-date 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-CRAN-date 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 

%description
Package for processing downloaded MODIS Cloud Product HDF files and
derived files. Specifically, MOD35_L2 cloud product files, and the
associated MOD03 geolocation files (for MODIS-TERRA); and MYD35_L2 cloud
product files, and the associated MYD03 geolocation files (for
MODIS-AQUA).  The package will be most effective if the user installs
MRTSwath (MODIS Reprojection Tool for swath products;
https://lpdaac.usgs.gov/tools/modis_reprojection_tool_swath), and adds the
directory with the MRTSwath executable to the default R PATH by editing
~/.Rprofile.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
