%global packname  RAINBOWR
%global packver   0.1.14
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.14
Release:          1%{?dist}
Summary:          Genome-Wide Association Study with SNP-Set Methods

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rrBLUP 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-tcltk 
BuildRequires:    R-Matrix 
BuildRequires:    R-cluster 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rrBLUP 
Requires:         R-CRAN-rgl 
Requires:         R-tcltk 
Requires:         R-Matrix 
Requires:         R-cluster 
Requires:         R-MASS 
Requires:         R-CRAN-pbmcapply 
Requires:         R-CRAN-optimx 
Requires:         R-methods 

%description
By using 'RAINBOWR' (Reliable Association INference By Optimizing Weights
with R), users can test multiple SNPs (Single Nucleotide Polymorphisms)
simultaneously by kernel-based (SNP-set) methods. This package can also be
applied to haplotype-based GWAS (Genome-Wide Association Study). Users can
test not only additive effects but also dominance and epistatic effects.
In detail, please check our preprint on bioRxiv: Kosuke Hamazaki and
Hiroyoshi Iwata (2019) <doi:10.1101/612028>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
