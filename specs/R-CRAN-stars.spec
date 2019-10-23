%global packname  stars
%global packver   0.4-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Spatiotemporal Arrays, Raster and Vector Data Cubes

License:          Apache License
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf >= 0.8.0
BuildRequires:    R-CRAN-classInt >= 0.4.1
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-sf >= 0.8.0
Requires:         R-CRAN-classInt >= 0.4.1
Requires:         R-CRAN-abind 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-lwgeom 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-units 

%description
Reading, manipulating, writing and plotting spatiotemporal arrays (raster
and vector data cubes) in 'R', using 'GDAL' bindings provided by 'sf', and
'NetCDF' bindings by 'ncmeta' and 'RNetCDF'.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/docker
%doc %{rlibdir}/%{packname}/nc
%doc %{rlibdir}/%{packname}/plumber
%doc %{rlibdir}/%{packname}/tif
%{rlibdir}/%{packname}/INDEX
