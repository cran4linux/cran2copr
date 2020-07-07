%global packname  birankr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Ranking Nodes in Bipartite and Weighted Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-data.table 
Requires:         R-Matrix 
Requires:         R-CRAN-data.table 

%description
Highly efficient functions for estimating various rank (centrality)
measures of nodes in bipartite graphs (two-mode networks). Includes
methods for estimating HITS, CoHITS, BGRM, and BiRank with implementation
primarily inspired by He et al. (2016) <doi:10.1109/TKDE.2016.2611584>.
Also provides easy-to-use tools for efficiently estimating PageRank in
one-mode graphs, incorporating or removing edge-weights during rank
estimation, projecting two-mode graphs to one-mode, and for converting
edgelists and matrices to sparseMatrix format. Best of all, the package's
rank estimators can work directly with common formats of network data
including edgelists (class data.frame, data.table, or tbl_df) and
adjacency matrices (class matrix or dgCMatrix).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
