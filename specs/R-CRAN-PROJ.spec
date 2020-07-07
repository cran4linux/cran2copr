%global packname  PROJ
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}
Summary:          Generic Coordinate System Transformations Using 'PROJ'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10

%description
A wrapper around the generic coordinate transformation software 'PROJ'
that transforms geospatial coordinates from one coordinate reference
system ('CRS') to another. This includes cartographic projections as well
as geodetic transformations. Version 6.0.0 or higher is required, earlier
versions if available are not used leaving this package harmlessly
non-functional. The intention is for this package to be used by
user-packages such as 'reproj', and that the older 'PROJ.4' and version 5
pathways be provided by the 'proj4' package. Separating this disruptive
version change (from 4.0 and 5.0, to 6.0 and above) allows the use of
existing and stable code in 'proj4' alongside the new idioms and
requirements of modern 'PROJ' using this package. The 'PROJ' library is
available from <https://proj.org/>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
