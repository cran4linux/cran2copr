%global packname  scanstatistics
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Space-Time Anomaly Detection using Scan Statistics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-emdbook 
BuildRequires:    R-CRAN-ismev 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-reliaR 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-emdbook 
Requires:         R-CRAN-ismev 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-reliaR 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Detection of anomalous space-time clusters using the scan statistics
methodology. Focuses on prospective surveillance of data streams, scanning
for clusters with ongoing anomalies. Hypothesis testing is made possible
by Monte Carlo simulation.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/image
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
