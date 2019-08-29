%global packname  ggraph
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          An Implementation of Grammar of Graphics for Graphs and Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggforce 
Requires:         R-grid 
Requires:         R-CRAN-scales 
Requires:         R-MASS 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-ggrepel 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-viridis 

%description
The grammar of graphics as implemented in ggplot2 is a poor fit for graph
and network visualizations due to its reliance on tabular data input.
ggraph is an extension of the ggplot2 API tailored to graph visualizations
and provides the same flexible approach to building up plots layer by
layer.

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
%doc %{rlibdir}/%{packname}/ggraph.png
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
