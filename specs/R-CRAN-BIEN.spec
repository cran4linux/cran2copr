%global packname  BIEN
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          3%{?dist}
Summary:          Tools for Accessing the Botanical Information and EcologyNetwork Database

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-RPostgreSQL 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-RPostgreSQL 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-ape 
Requires:         R-methods 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-fasterize 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Provides Tools for Accessing the Botanical Information and Ecology Network
Database.  The BIEN database contains cleaned and standardized botanical
data including occurrence, trait, plot and taxonomic data (See
<http://Bien.nceas.ucsb.edu/bien/> for more Information).  This package
provides functions that query the BIEN database by constructing and
executing optimized SQL queries.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
