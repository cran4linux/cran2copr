%global packname  selac
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          2%{?dist}
Summary:          Selection Models for Amino Acid and/or Codon Evolution

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-nloptr 
Requires:         R-nnet 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-expm 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-RColorBrewer 

%description
Sets up and executes a SelAC model (Selection on Amino acids and codons)
for testing the presence of selection in amino acid or codon among a set
of genes on a fixed phylogeny. Beaulieu et al (2019)
<doi:10.1093/molbev/msy222>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
