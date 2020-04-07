%global packname  rGEDI
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          NASA's Global Ecosystem Dynamics Investigation (GEDI) DataVisualization and Processing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hdf5r 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hdf5r 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
Set of tools for downloading, reading, visualizing and processing GEDI
Level1B, Level2A and Level2B data.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/m4
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
