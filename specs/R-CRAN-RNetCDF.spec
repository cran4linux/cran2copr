%global packname  RNetCDF
%global packver   2.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Interface to 'NetCDF' Datasets

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    netcdf-devel udunits2-devel
Requires:         netcdf udunits2
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0

%description
An interface to the 'NetCDF' file formats designed by Unidata for
efficient storage of array-oriented scientific data and descriptions. Most
capabilities of 'NetCDF' version 4 are supported. Optional conversions of
time units are enabled by 'UDUNITS' version 2, also from Unidata.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/udunits
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
