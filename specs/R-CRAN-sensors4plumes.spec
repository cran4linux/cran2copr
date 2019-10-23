%global packname  sensors4plumes
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          Test and Optimise Sampling Designs Based on Plume Simulations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-emdist 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-conf.design 
BuildRequires:    R-CRAN-automap 
BuildRequires:    R-CRAN-genalg 
Requires:         R-methods 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 
Requires:         R-lattice 
Requires:         R-CRAN-emdist 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-FNN 
Requires:         R-graphics 
Requires:         R-CRAN-conf.design 
Requires:         R-CRAN-automap 
Requires:         R-CRAN-genalg 

%description
Test sampling designs by several flexible cost functions, usually based on
the simulations, and optimise sampling designs using different
optimisation algorithms; load plume simulations (on lattice or points)
even if they do not fit into memory.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
