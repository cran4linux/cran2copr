%global packname  landscapeR
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Categorical Landscape Simulation Facility

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-Rcpp 

%description
Simulates categorical maps on actual geographical realms, starting from
either empty landscapes or landscapes provided by the user (e.g. land use
maps). Allows to tweak or create landscapes while retaining a high degree
of control on its features, without the hassle of specifying each location
attribute. In this it differs from other tools which generate null or
neutral landscapes in a theoretical space. The basic algorithm currently
implemented uses a simple agent style/cellular automata growth model, with
no rules (apart from areas of exclusion) and von Neumann neighbourhood
(four cells, aka Rook case). Outputs are raster dataset exportable to any
common GIS format.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
