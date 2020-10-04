%global packname  leafsync
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Small Multiples for Leaflet Web Maps

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.1
BuildRequires:    R-CRAN-htmltools >= 0.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-htmlwidgets 
Requires:         R-CRAN-leaflet >= 2.0.1
Requires:         R-CRAN-htmltools >= 0.3
Requires:         R-methods 
Requires:         R-CRAN-htmlwidgets 

%description
Create small multiples of several leaflet web maps with (optional)
synchronised panning and zooming control. When syncing is enabled all maps
respond to mouse actions on one map. This allows side-by-side comparisons
of different attributes of the same geometries. Syncing can be adjusted so
that any combination of maps can be synchronised.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
