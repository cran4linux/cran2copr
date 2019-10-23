%global packname  ncmeta
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Straightforward 'NetCDF' Metadata

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RNetCDF 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RNetCDF 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 

%description
Extract metadata from 'NetCDF' data sources, these can be files, file
handles or servers. This package leverages and extends the lower level
functions of the 'RNetCDF' package providing a consistent set of functions
that all return data frames. We introduce named concepts of 'grid', 'axis'
and 'source' which are all meaningful entities without formal definition
in the 'NetCDF' library <https://www.unidata.ucar.edu/software/netcdf/>.
'RNetCDF' matches the library itself with only the named concepts of
'variables', 'dimensions' and 'attributes'. 'ncmeta' provides a required
framework for the in-development 'tidync' project
<https://github.com/hypertidy/tidync>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/eke-speed
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/flowchart
%doc %{rlibdir}/%{packname}/test-RNetCDF
%{rlibdir}/%{packname}/INDEX
