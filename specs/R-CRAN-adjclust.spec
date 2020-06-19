%global packname  adjclust
%global packver   0.5.99
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.99
Release:          1%{?dist}
Summary:          Adjacency-Constrained Clustering of a Block-Diagonal SimilarityMatrix

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-capushe 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-Matrix 
Requires:         R-CRAN-matrixStats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-capushe 

%description
Implements a constrained version of hierarchical agglomerative clustering,
in which each observation is associated to a position, and only adjacent
clusters can be merged. Typical application fields in bioinformatics
include Genome-Wide Association Studies or Hi-C data analysis, where the
similarity between items is a decreasing function of their genomic
distance. Taking advantage of this feature, the implemented algorithm is
time and memory efficient. This algorithm is described in Ambroise et al
(2019)
<https://almob.biomedcentral.com/articles/10.1186/s13015-019-0157-4>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/system
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
