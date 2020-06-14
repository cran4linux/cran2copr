%global packname  eesim
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Simulate and Evaluate Time Series for Environmental Epidemiology

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.5.6
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-viridis >= 0.4.0
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-splines 
Requires:         R-CRAN-lubridate >= 1.5.6
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-viridis >= 0.4.0
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-splines 

%description
Provides functions to create simulated time series of environmental
exposures (e.g., temperature, air pollution) and health outcomes for use
in power analysis and simulation studies in environmental epidemiology.
This package also provides functions to evaluate the results of simulation
studies based on these simulated time series. This work was supported by a
grant from the National Institute of Environmental Health Sciences
(R00ES022631) and a fellowship from the Colorado State University Programs
for Research and Scholarly Excellence.

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
%{rlibdir}/%{packname}/INDEX
