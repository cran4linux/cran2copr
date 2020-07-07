%global packname  mapview
%global packver   2.7.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.8
Release:          3%{?dist}
Summary:          Interactive Viewing of Spatial Data in R

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.0
BuildRequires:    R-CRAN-scales >= 0.2.5
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-leafem 
BuildRequires:    R-CRAN-leafpop 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-satellite 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-webshot 
Requires:         R-CRAN-leaflet >= 2.0.0
Requires:         R-CRAN-scales >= 0.2.5
Requires:         R-methods 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-lattice 
Requires:         R-CRAN-leafem 
Requires:         R-CRAN-leafpop 
Requires:         R-CRAN-png 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-satellite 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-webshot 

%description
Quickly and conveniently create interactive visualisations of spatial data
with or without background maps. Attributes of displayed features are
fully queryable via pop-up windows. Additional functionality includes
methods to visualise true- and false-color raster images and bounding
boxes.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
