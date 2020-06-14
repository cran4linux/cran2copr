%global packname  GISTools
%global packver   0.7-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          2%{?dist}
Summary:          Some further GIS capabilities for R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rgeos 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-MASS 
Requires:         R-CRAN-rgeos 

%description
Some mapping and spatial data manipulation tools - in particular drawing
choropleth maps with nice looking legends, and aggregation of point data
to polygons.

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
