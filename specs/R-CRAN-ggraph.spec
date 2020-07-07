%global packname  ggraph
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          3%{?dist}
Summary:          An Implementation of Grammar of Graphics for Graphs and Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-graphlayouts >= 0.5.0
BuildRequires:    R-CRAN-ggforce >= 0.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.2
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidygraph 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-graphlayouts >= 0.5.0
Requires:         R-CRAN-ggforce >= 0.3.1
Requires:         R-CRAN-Rcpp >= 0.12.2
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-scales 
Requires:         R-MASS 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-ggrepel 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidygraph 

%description
The grammar of graphics as implemented in ggplot2 is a poor fit for graph
and network visualizations due to its reliance on tabular data input.
ggraph is an extension of the ggplot2 API tailored to graph visualizations
and provides the same flexible approach to building up plots layer by
layer.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
