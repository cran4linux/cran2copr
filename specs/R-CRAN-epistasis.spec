%global packname  epistasis
%global packver   0.0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1.1
Release:          2%{?dist}
Summary:          Detecting Epistatic Selection with Partially Observed GenotypeData

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-methods 

%description
An efficient multi-core package to reconstruct an underlying network of
genomic signatures of high-dimensional epistatic selection from partially
observed genotype data. The phenotype that we consider is viability. The
network captures the conditional dependent short- and long-range linkage
disequilibrium structure of genomes and thus reveals aberrant
marker-marker associations that are due to epistatic selection. We target
on high-dimensional genotype data where number of variables (markers) is
larger than number of sample sizes (p >> n). The computations is
memory-optimized using the sparse matrix output.

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
%{rlibdir}/%{packname}/INDEX
