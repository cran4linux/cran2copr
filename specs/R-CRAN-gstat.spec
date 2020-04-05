%global packname  gstat
%global packver   2.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}
Summary:          Spatial and Spatio-Temporal Geostatistical Modelling, Predictionand Simulation

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-spacetime >= 1.0.0
BuildRequires:    R-CRAN-sp >= 0.9.72
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-FNN 
Requires:         R-CRAN-spacetime >= 1.0.0
Requires:         R-CRAN-sp >= 0.9.72
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-lattice 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-FNN 

%description
Variogram modelling; simple, ordinary and universal point or block
(co)kriging; spatio-temporal kriging; sequential Gaussian or indicator
(co)simulation; variogram and variogram map plotting utility functions;
supports sf and stars.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/external
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
