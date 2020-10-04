%global packname  FESta
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fishing Effort Standardisation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Original idea was presented in the reference paper. Varghese et al. (2020,
74(1):35-42) "Bayesian State-space Implementation of Schaefer Production
Model for Assessment of Stock Status for Multi-gear Fishery". Marine
fisheries governance and management practices are very essential to ensure
the sustainability of the marine resources. A widely accepted resource
management strategy towards this is to derive sustainable fish harvest
levels based on the status of marine fish stock. Various fish stock
assessment models that describe the biomass dynamics using time series
data on fish catch and fishing effort are generally used for this purpose.
In the scenario of complex multi-species marine fishery in which different
species are caught by a number of fishing gears and each gear harvests a
number of species make it difficult to obtain the fishing effort
corresponding to each fish species. Since the capacity of the gears
varies, the effort made to catch a resource cannot be considered as the
sum of efforts expended by different fishing gears. This necessitates
standardisation of fishing effort in unit base.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
