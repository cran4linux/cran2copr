%global packname  bfsMaps
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          2%{?dist}
Summary:          Plot Maps from Switzerland by Swiss Federal Statistical Office

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-methods 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-DescTools 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rlang 
Requires:         R-methods 

%description
At the Swiss Federal Statistical Office (SFSO), spatial maps of
Switzerland are available free of charge as 'Cartographic bases for
small-scale thematic mapping'. This package contains convenience functions
to import ESRI (Environmental Systems Research Institute) shape files
using the package 'rgdal' and to plot them easily and quickly without
having to worry too much about the technical details. It contains
utilities to combine multiple areas to one single polygon and to find
neighbours for single regions. For any point on a map, a special locator
can be used to determine to which municipality, district or canton it
belongs.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
