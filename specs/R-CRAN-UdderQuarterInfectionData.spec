%global packname  UdderQuarterInfectionData
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Udder Quarter Infection Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
The udder quarter infection data set contains infection times of
individual cow udder quarters with Corynebacterium bovis (Laevens et al.
1997 <DOI:10.3168/jds.S0022-0302(97)76295-7>). Obviously, the four udder
quarters are clustered within a cow, and udder quarters are sampled only
approximately monthly, generating interval-censored data. The data set
contains both covariates that change within a cow (e.g., front and rear
udder quarters) and covariates that change between cows (e.g., parity [the
number of previous calvings]). The correlation between udder infection
times within a cow also is of interest, because this is a measure of the
infectivity of the agent causing the disease. Various models have been
applied to address the problem of interdependence for right-censored event
times. These models, as applied to this data set, can be found back in the
publications found in the reference list.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
