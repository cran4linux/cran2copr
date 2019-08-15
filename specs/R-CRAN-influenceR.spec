%global packname  influenceR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Software Tools to Quantify Structural Importance of Nodes in aNetwork

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-Matrix >= 1.1.4
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-Matrix >= 1.1.4
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-methods 
Requires:         R-utils 

%description
Provides functionality to compute various node centrality measures on
networks. Included are functions to compute betweenness centrality (by
utilizing Madduri and Bader's SNAP library), implementations of Burt's
constraint and effective network size (ENS) metrics, Borgatti's algorithm
to identify key players, and Valente's bridging metric. On Unix systems,
the betweenness, Key Players, and bridging implementations are
parallelized with OpenMP, which may run faster on systems which have
OpenMP configured.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
