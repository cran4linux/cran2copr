%global packname  PhyloMeasures
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}
Summary:          Fast and Exact Algorithms for Computing PhylogeneticBiodiversity Measures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-methods 
Requires:         R-CRAN-ape 
Requires:         R-methods 

%description
Given a phylogenetic tree T and an assemblage S of species represented as
a subset of tips in T, we want to compute a measure of the diversity of
the species in S with respect to T. The current package offers efficient
algorithms that can process large phylogenetic data for several such
measures. Most importantly, the package includes algorithms for computing
efficiently the standardized versions of phylogenetic measures and their
p-values, which are essential for null model comparisons. Among other
functions, the package provides efficient computation of
richness-standardized versions for indices such as the net relatedness
index (NRI), nearest taxon index (NTI), phylogenetic diversity index
(PDI), and the corresponding indices of two-sample measures. The package
also introduces a new single-sample measure, the Core Ancestor Cost (CAC);
the package provides functions for computing the value and the
standardised index of the CAC and, more than that, there is an extra
function available that can compute exactly any statistical moment of the
measure. The package supports computations under different null models,
including abundance-weighted models.

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
