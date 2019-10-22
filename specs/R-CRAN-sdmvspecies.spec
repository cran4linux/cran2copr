%global packname  sdmvspecies
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Create Virtual Species for Species Distribution Modelling

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-psych 
Requires:         R-parallel 

%description
A software package help user to create virtual species for species
distribution modelling. It includes several methods to help user to create
virtual species distribution map. Those maps can be used for Species
Distribution Modelling (SDM) study. SDM use environmental data for sites
of occurrence of a species to predict all the sites where the
environmental conditions are suitable for the species to persist, and may
be expected to occur.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/external
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
