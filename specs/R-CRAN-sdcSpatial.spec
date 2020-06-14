%global packname  sdcSpatial
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Statistical Disclosure Control for Spatial Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
Requires:         R-CRAN-raster 
Requires:         R-methods 

%description
Privacy protected raster maps can be created from spatial point data.
Protection methods include smoothing of dichotomous variables by de Jonge
and de Wolf (2016) <doi:10.1007/978-3-319-45381-1_9>, continuous variables
by de Wolf and de Jonge (2018) <doi:10.1007/978-3-319-99771-1_23>,
suppressing revealing values and a generalization of the quad tree method
by Suñé, Rovira, Ibáñez and Farré (2017) <doi:10.2901/EUROSTAT.C2017.001>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/app
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
