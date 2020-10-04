%global packname  carcass
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation of the Number of Fatalities from Carcass Searches

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-survival 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-arm 
Requires:         R-MASS 

%description
The number of bird or bat fatalities from collisions with buildings,
towers or wind energy turbines can be estimated based on carcass searches
and experimentally assessed carcass persistence times and searcher
efficiency. Functions for estimating the probability that a bird or bat
that died is found by a searcher are provided. Further functions calculate
the posterior distribution of the number of fatalities based on the number
of carcasses found and the estimated detection probability.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
