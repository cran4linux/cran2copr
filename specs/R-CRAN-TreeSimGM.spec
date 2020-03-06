%global packname  TreeSimGM
%global packver   2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5
Release:          1%{?dist}
Summary:          Simulating Phylogenetic Trees under General Bellman Harris andLineage Shift Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-TreeSim 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-methods 
Requires:         R-CRAN-TreeSim 
Requires:         R-CRAN-ape 
Requires:         R-methods 

%description
Provides a flexible simulation tool for phylogenetic trees under a general
model for speciation and extinction. Trees with a user-specified number of
extant tips, or a user-specified stem age are simulated. It is possible to
assume any probability distribution for the waiting time until speciation
and extinction. Furthermore, the waiting times to speciation / extinction
may be scaled in different parts of the tree, meaning we can simulate
trees with clade-dependent diversification processes. At a speciation
event, one species splits into two. We allow for two different modes at
these splits: (i) symmetric, where for every speciation event new waiting
times until speciation and extinction are drawn for both daughter
lineages; and (ii) asymmetric, where a speciation event results in one
species with new waiting times, and another that carries the extinction
time and age of its ancestor. The symmetric mode can be seen as an
vicariant or allopatric process where divided populations suffer equal
evolutionary forces while the asymmetric mode could be seen as a
peripatric speciation where a mother lineage continues to exist.
Reference: O. Hagen and T. Stadler (2017). TreeSimGM: Simulating
phylogenetic trees under general Bellman Harris models with
lineage-specific shifts of speciation and extinction in R. Methods in
Ecology and Evolution. <doi:10.1111/2041-210X.12917>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
