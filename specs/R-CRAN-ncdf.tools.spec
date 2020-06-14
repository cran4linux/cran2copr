%global packname  ncdf.tools
%global packver   0.7.1.295
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1.295
Release:          2%{?dist}
Summary:          Easier 'NetCDF' File Handling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RNetCDF 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-JBTools 
Requires:         R-CRAN-RNetCDF 
Requires:         R-CRAN-chron 
Requires:         R-parallel 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-JBTools 

%description
Set of tools to simplify the handling of 'NetCDF' files with the 'RNetCDF'
package. Most functions are wrappers of basic functions from the 'RNetCDF'
package to easily run combinations of these functions for frequently
encountered tasks.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
