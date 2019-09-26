%global packname  tnam
%global packver   1.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          1%{?dist}
Summary:          Temporal Network Autocorrelation Models (TNAM)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-xergm.common >= 1.7.7
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-xergm.common >= 1.7.7
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-network 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-vegan 

%description
Temporal and cross-sectional network autocorrelation models. These are
models for variation in attributes of nodes nested in a network (e.g.,
drinking behavior of adolescents nested in a school class, or democracy
versus autocracy of countries nested in the network of international
relations). These models can be estimated for cross-sectional data or
panel data, with complex network dependencies as predictors, multiple
networks and covariates, arbitrary outcome distributions, and random
effects or time trends. Basic references: Doreian, Teuter and Wang (1984)
<doi:10.1177/0049124184013002001>; Hays, Kachi and Franzese (2010)
<doi:10.1016/j.stamet.2009.11.005>; Leenders, Roger Th. A. J. (2002)
<doi:10.1016/S0378-8733(01)00049-1>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
