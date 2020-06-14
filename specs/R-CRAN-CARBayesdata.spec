%global packname  CARBayesdata
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}
Summary:          Data Used in the Vignettes Accompanying the CARBayes andCARBayesST Packages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-shapefiles 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-shapefiles 

%description
Spatio-temporal data from Scotland used in the vignettes accompanying the
CARBayes (spatial modelling) and CARBayesST (spatio-temporal modelling)
packages. All data except for the Scottish lip cancer data relate to the
set of 271 Intermediate Geographies (IG, but also known as Intermediate
Zones (IZ)) that make up the 2001 definition of the Greater Glasgow and
Clyde health board.

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
%{rlibdir}/%{packname}/INDEX
