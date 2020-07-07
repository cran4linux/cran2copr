%global packname  fingerPro
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Sediment Source Fingerprinting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS >= 7.3.45
BuildRequires:    R-grid >= 3.1.1
BuildRequires:    R-CRAN-car >= 3.0.0
BuildRequires:    R-CRAN-Rcmdr >= 2.4.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-GGally >= 1.3.2
BuildRequires:    R-CRAN-rgl >= 0.99.9
BuildRequires:    R-CRAN-reshape >= 0.8.7
BuildRequires:    R-CRAN-klaR >= 0.6.12
BuildRequires:    R-CRAN-scales >= 0.5.0
BuildRequires:    R-CRAN-RcppProgress >= 0.4
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-MASS >= 7.3.45
Requires:         R-grid >= 3.1.1
Requires:         R-CRAN-car >= 3.0.0
Requires:         R-CRAN-Rcmdr >= 2.4.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-GGally >= 1.3.2
Requires:         R-CRAN-rgl >= 0.99.9
Requires:         R-CRAN-reshape >= 0.8.7
Requires:         R-CRAN-klaR >= 0.6.12
Requires:         R-CRAN-scales >= 0.5.0
Requires:         R-CRAN-RcppProgress >= 0.4
Requires:         R-CRAN-Rcpp >= 0.11.3

%description
Quantifies the provenance of the sediments in a catchment or study area.
Based on a comprehensive characterization of the sediment sources and the
end sediment mixtures a mixing model algorithm is applied to the sediment
mixtures in order to estimate the relative contribution of each potential
source. The package includes several statistical methods such as
Kruskal-Wallis test, discriminant function analysis ('DFA'), principal
component plot ('PCA') to select the optimal subset of tracer properties.
The variability within each sediment source is also considered to estimate
the statistical distribution of the sources contribution.

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
