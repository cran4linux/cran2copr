%global packname  lakemorpho
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          2%{?dist}
Summary:          Lake Morphometry Metrics

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-cluster 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geosphere 
Requires:         R-cluster 

%description
Lake morphometry metrics are used by limnologists to understand, among
other things, the ecological processes in a lake. Traditionally, these
metrics are calculated by hand, with planimeters, and increasingly with
commercial GIS products. All of these methods work; however, they are
either outdated, difficult to reproduce, or require expensive licenses to
use. The 'lakemorpho' package provides the tools to calculate a typical
suite of these metrics from an input elevation model and lake polygon. The
metrics currently supported are: fetch, major axis, minor axis,
major/minor axis ratio, maximum length, maximum width, mean width, maximum
depth, mean depth, shoreline development, shoreline length, surface area,
and volume.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
