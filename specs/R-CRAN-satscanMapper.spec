%global packname  satscanMapper
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          'SaTScan' (TM) Results Mapper

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-SeerMapper 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-foreign 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-methods 
Requires:         R-CRAN-SeerMapper 

%description
Supports the generation of maps based on the results from 'SaTScan' (TM)
cluster analysis. The package handles mapping of Spatial and Spatial-Time
analysis using the discrete Poisson, Bernoulli, and exponential models of
case data generating cluster and location ('GIS') records containing
observed, expected and observed/expected ratio for U. S. states (and DC),
counties or census tracts of individual states based on the U. S. 'FIPS'
codes for state, county and census tracts (locations) using 2000 or 2010
Census areas, 'FIPS' codes, and boundary data. 'satscanMapper' uses the
'SeerMapper' package for the boundary data and mapping of locations.  Not
all of the 'SaTScan' (TM) analysis and models generate the observed,
expected and observed/expected ratio values for the clusters and
locations. The user can map the observed/expected ratios for locations
(states, counties, or census tracts) for each cluster with a p-value less
than 0.05 or a user specified p-value. The locations are categorized and
colored based on either the cluster's Observed/Expected ratio or the
locations' Observed/Expected ratio. The place names are provided for each
census tract using data from 'NCI', the 'HUD' crossover tables (Tract to
Zip code) as of December, 2013, the USPS Zip code 5 database for 1999, and
manual look ups on the USPS.gov web site.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATIONS
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
