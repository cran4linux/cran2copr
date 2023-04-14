%global __brp_check_rpaths %{nil}
%global packname  rbison
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to the 'USGS' 'BISON' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.1
BuildRequires:    R-CRAN-crul >= 0.7.4
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-jsonlite >= 1.1
Requires:         R-CRAN-crul >= 0.7.4
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mapproj 
Requires:         R-grid 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-tibble 

%description
Interface to the 'USGS' 'BISON' (<https://bison.usgs.gov/>) API, a
'database' for species occurrence data. Data comes from species in the
United States from participating data providers. You can get data via
'taxonomic' and location based queries. A simple function is provided to
help visualize data.

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
%{rlibdir}/%{packname}
