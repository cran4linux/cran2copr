%global __brp_check_rpaths %{nil}
%global packname  proccalibrad
%global packver   0.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14
Release:          3%{?dist}%{?buildtag}
Summary:          Extraction of Bands from MODIS Calibrated Radiances MOD02 NRT

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Package for processing downloaded MODIS Calibrated radiances Product HDF
files. Specifically, MOD02 calibrated radiance product files, and the
associated MOD03 geolocation files (for MODIS-TERRA). The package will be
most effective if the user installs MRTSwath (MODIS Reprojection Tool for
swath products;
<https://lpdaac.usgs.gov/tools/modis_reprojection_tool_swath>, and adds
the directory with the MRTSwath executable to the default R PATH by
editing ~/.Rprofile.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
