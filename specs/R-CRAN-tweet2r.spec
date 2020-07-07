%global packname  tweet2r
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Twitter Collector for R and Export to 'SQLite', 'postGIS' and'GIS' Format

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ROAuth 
BuildRequires:    R-CRAN-streamR 
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-spacetime 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-maptools 
Requires:         R-CRAN-ROAuth 
Requires:         R-CRAN-streamR 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-spacetime 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-maptools 

%description
This is an improved implementation of the package 'StreamR' to capture
tweets and store it into R, SQLite, 'postGIS' data base or GIS format. The
package performs a description of harvested data and performs space time
exploratory analysis.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
