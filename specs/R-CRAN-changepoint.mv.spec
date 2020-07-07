%global packname  changepoint.mv
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Changepoint Analysis for Multivariate Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-tbart 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-assertive 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-methods 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-tbart 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-assertive 

%description
Detects the Most Recent Changepoints (mrc) for panel data consisting of
many related univariate timeseries using the method developed by Bardwell,
Fearnhead, Eckley, Smith and Spott (2018)
<doi:10.1080/00401706.2018.1438926>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
