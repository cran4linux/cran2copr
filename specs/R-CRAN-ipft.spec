%global packname  ipft
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          3%{?dist}
Summary:          Indoor Positioning Fingerprinting Toolset

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-apcluster 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-apcluster 
Requires:         R-cluster 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 

%description
Algorithms and utility functions for indoor positioning using
fingerprinting techniques. These functions are designed for manipulation
of RSSI (Received Signal Strength Intensity) data sets, estimation of
positions,comparison of the performance of different models, and graphical
visualization of data. Machine learning algorithms and methods such as
k-nearest neighbors or probabilistic fingerprinting are implemented in
this package to perform analysis and estimations over RSSI data sets.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
