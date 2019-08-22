%global packname  pegas
%global packver   0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11
Release:          1%{?dist}
Summary:          Population and Evolutionary Genetics Analysis System

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildRequires:    R-CRAN-ape >= 2.4
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape >= 2.4
Requires:         R-CRAN-adegenet 
Requires:         R-graphics 
Requires:         R-utils 

%description
Functions for reading, writing, plotting, analysing, and manipulating
allelic and haplotypic data, including from VCF files, and for the
analysis of population nucleotide sequences and micro-satellites including
coalescent analyses, linkage disequilibrium, population structure (Fst,
Amova) and equilibrium (HWE), haplotype networks, minimum spanning tree
and network, and median-joining networks.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
