%global packname  Rnets
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Resistance Relationship Networks using Graphical LASSO

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-glasso >= 1.8
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-igraph >= 1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-glasso >= 1.8
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-igraph >= 1.0
Requires:         R-methods 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-rlang 

%description
Novel methods are needed to analyze the large amounts of antimicrobial
resistance (AMR) data generated by AMR surveillance programs. This package
is used to estimate resistance relationship networks, or 'Rnets', from
empirical antimicrobial susceptibility data. These networks can be used to
study relationships between antimicrobial resistances (typically measured
using MICs) and genes in populations. The 'GitHub' for this package is
available at <https://GitHub.com/EpidemiologyDVM/Rnets>. Bug reports and
features requests should be directed to the same 'GitHub' site. The
methods used in 'Rnets' are available in the following publications: An
overview of the method in WJ Love, et al., "Markov Networks of Collateral
Resistance: National Antimicrobial Resistance Monitoring System
Surveillance Results from Escherichia coli Isolates, 2004-2012" (2016)
<doi:10.1371/journal.pcbi.1005160>; The graphical LASSO for sparsity in J
Friedman, T Hastie, R Tibshirani "Sparse inverse covariance estimation
with the graphical lasso" (2007) <doi:10.1093/biostatistics/kxm045>; L1
penalty selection in H Liu, K Roeder, L Wasserman "Stability Approach to
Regularization Selection (StARS) for High Dimensional Graphical Models"
(2010) <arXiv:1006.3316>; Modularity for graphs with negative edge weights
in S Gomez, P Jensen, A Arenas. "Analysis of community structure in
networks of correlated data" (2009) <doi:10.1103/PhysRevE.80.016114>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
