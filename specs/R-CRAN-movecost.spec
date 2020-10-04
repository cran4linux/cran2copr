%global packname  movecost
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Calculation of Accumulated Cost Surface and Least-Cost PathsRelated to Human Movement Across the Landscape

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.8.4
BuildRequires:    R-CRAN-rgdal >= 1.3.6
BuildRequires:    R-CRAN-sp >= 1.3.1
BuildRequires:    R-CRAN-gdistance >= 1.2.2
BuildRequires:    R-CRAN-rgeos >= 0.4.2
Requires:         R-CRAN-raster >= 2.8.4
Requires:         R-CRAN-rgdal >= 1.3.6
Requires:         R-CRAN-sp >= 1.3.1
Requires:         R-CRAN-gdistance >= 1.2.2
Requires:         R-CRAN-rgeos >= 0.4.2

%description
Provides the facility to calculate non-isotropic accumulated cost surface
and least-cost paths using a number of human-movement-related cost
functions that can be selected by the user. It just requires a Digital
Terrain Model, a start location and (optionally) destination locations.
See Alberti (2019) <doi:10.1016/j.softx.2019.100331>.

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
%{rlibdir}/%{packname}/INDEX
