%global packname  ncdf4
%global packver   1.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.17
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to Unidata netCDF (Version 4 or Earlier) Format DataFiles

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    netcdf-devel >= 4.1
Requires:         netcdf
BuildRequires:    R-devel
Requires:         R-core

%description
Provides a high-level R interface to data files written using Unidata's
netCDF library (version 4 or earlier), which are binary data files that
are portable across platforms and include metadata information in addition
to the data sets.  Using this package, netCDF files (either version 4 or
"classic" version 3) can be opened and data sets read in easily.  It is
also easy to create new netCDF dimensions, variables, and files, in either
version 3 or 4 format, and manipulate existing netCDF files.  This package
replaces the former ncdf package, which only worked with netcdf version 3
files.  For various reasons the names of the functions have had to be
changed from the names in the ncdf package.  The old ncdf package is still
available at the URL given below, if you need to have backward
compatibility.  It should be possible to have both the ncdf and ncdf4
packages installed simultaneously without a problem.  However, the ncdf
package does not provide an interface for netcdf version 4 files.

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
%doc %{rlibdir}/%{packname}/HDF5_COPYING
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
