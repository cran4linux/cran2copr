%global packname  LBSPR
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Length-Based Spawning Potential Ratio

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-methods 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-tidyr 

%description
Simulate expected equilibrium length composition, yield-per-recruit, and
the spawning potential ratio (SPR) using the length-based SPR (LBSPR)
model. Fit the LBSPR model to length data to estimate selectivity,
relative apical fishing mortality, and the spawning potential ratio for
data-limited fisheries. See Hordyk et al (2016)
<doi:10.1139/cjfas-2015-0422> for more information about the LBSPR
assessment method.

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
%doc %{rlibdir}/%{packname}/LFreq_MultiYr.csv
%doc %{rlibdir}/%{packname}/LFreq_MultiYrHead.csv
%doc %{rlibdir}/%{packname}/LFreq_SingYr.csv
%doc %{rlibdir}/%{packname}/LFreq_SingYrHead.csv
%doc %{rlibdir}/%{packname}/LRaw_MultiYr.csv
%doc %{rlibdir}/%{packname}/LRaw_MultiYrHead.csv
%doc %{rlibdir}/%{packname}/LRaw_SingYr.csv
%doc %{rlibdir}/%{packname}/LRaw_SingYrHead.csv
%doc %{rlibdir}/%{packname}/shiny_apps
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
