%global packname  tidygraph
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}
Summary:          A Tidy API for Graph Manipulation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-pillar 
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-pillar 

%description
A graph, while not "tidy" in itself, can be thought of as two tidy data
frames describing node and edge data respectively. 'tidygraph' provides an
approach to manipulate these two virtual data frames using the API defined
in the 'dplyr' package, as well as provides tidy interfaces to a lot of
common graph algorithms.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
