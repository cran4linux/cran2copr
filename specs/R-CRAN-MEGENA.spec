%global packname  MEGENA
%global packver   1.3.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.7
Release:          3%{?dist}%{?buildtag}
Summary:          Multiscale Clustering of Geometrical Network

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-fpc >= 2.1.11
BuildRequires:    R-cluster >= 2.0.7.1
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-igraph >= 1.2.1
BuildRequires:    R-Matrix >= 1.1.5
BuildRequires:    R-CRAN-doParallel >= 1.0.11
BuildRequires:    R-CRAN-ggraph >= 1.0.1
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-reshape >= 0.8.5
BuildRequires:    R-CRAN-ggrepel >= 0.5
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-fpc >= 2.1.11
Requires:         R-cluster >= 2.0.7.1
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-igraph >= 1.2.1
Requires:         R-Matrix >= 1.1.5
Requires:         R-CRAN-doParallel >= 1.0.11
Requires:         R-CRAN-ggraph >= 1.0.1
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-reshape >= 0.8.5
Requires:         R-CRAN-ggrepel >= 0.5
Requires:         R-CRAN-Rcpp >= 0.11.3

%description
Co-Expression Network Analysis by adopting network embedding technique.
Song W.-M., Zhang B. (2015) Multiscale Embedded Gene Co-expression Network
Analysis. PLoS Comput Biol 11(11): e1004574. <doi:
10.1371/journal.pcbi.1004574>.

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
%{rlibdir}/%{packname}/libs
