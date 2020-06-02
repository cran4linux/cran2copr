%global packname  phytools
%global packver   0.7-47
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.47
Release:          1%{?dist}
Summary:          Phylogenetic Tools for Comparative Biology (and Other Things)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 4.0
BuildRequires:    R-CRAN-phangorn >= 2.3.1
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape >= 4.0
Requires:         R-CRAN-phangorn >= 2.3.1
Requires:         R-CRAN-maps 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-expm 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gtools 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-mnormt 
Requires:         R-nlme 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-stats 
Requires:         R-utils 

%description
A wide range of functions for phylogenetic analysis. Functionality is
concentrated in phylogenetic comparative biology, but also includes
numerous methods for visualizing, manipulating, reading or writing, and
even inferring phylogenetic trees and data. Included among the functions
in phylogenetic comparative biology are various for ancestral state
reconstruction, model-fitting, simulation of phylogenies and data, and
multivariate analysis. There are a broad range of plotting methods for
phylogenies and comparative data which include, but are not restricted to,
methods for mapping trait evolution on trees, for projecting trees into
phenotypic space or a geographic map, and for visualizing correlated
speciation between trees. Finally, there are a number of functions for
reading, writing, analyzing, inferring, simulating, and manipulating
phylogenetic trees and comparative data not covered by other packages. For
instance, there are functions for randomly or non-randomly attaching
species or clades to a phylogeny, for estimating supertrees or consensus
phylogenies from a set, for simulating trees and phylogenetic data under a
range of models, and for a wide variety of other manipulations and
analyses that phylogenetic biologists might find useful in their research.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
