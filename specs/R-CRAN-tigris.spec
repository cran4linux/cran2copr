%global packname  tigris
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          3%{?dist}
Summary:          Load Census TIGER/Line Shapefiles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-utils 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 

%description
Download TIGER/Line shapefiles from the United States Census Bureau
(<https://www.census.gov/geo/maps-data/data/tiger-line.html>) and load
into R as 'SpatialDataFrame' or 'sf' objects.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
