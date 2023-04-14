%global __brp_check_rpaths %{nil}
%global packname  redlistr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for the IUCN Red List of Ecosystems and Species

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-sp >= 1.2.4
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rgeos 
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-sp >= 1.2.4
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rgeos 

%description
A toolbox created by members of the International Union for Conservation
of Nature (IUCN) Red List of Ecosystems Committee for Scientific
Standards. Primarily, it is a set of tools suitable for calculating the
metrics required for making assessments of species and ecosystems against
the IUCN Red List of Threatened Species and the IUCN Red List of
Ecosystems categories and criteria. See the IUCN website for detailed
guidelines, the criteria, publications and other information.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
