%global packname  ncdf4.helpers
%global packver   0.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          3%{?dist}
Summary:          Helper Functions for Use with the 'ncdf4' Package

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-PCICt 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-PCICt 
Requires:         R-CRAN-abind 

%description
Contains a collection of helper functions for dealing with 'NetCDF' files
<https://www.unidata.ucar.edu/software/netcdf/> opened using 'ncdf4',
particularly 'NetCDF' files that conform to the Climate and Forecast (CF)
Metadata Conventions
<http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html>.

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
%{rlibdir}/%{packname}/INDEX
