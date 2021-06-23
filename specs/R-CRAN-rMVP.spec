%global __brp_check_rpaths %{nil}
%global packname  rMVP
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Memory-Efficient, Visualize-Enhanced, Parallel-Accelerated GWAS Tool

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-BH 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-bigmemory 

%description
A memory-efficient, visualize-enhanced, parallel-accelerated Genome-Wide
Association Study (GWAS) tool. It can (1) effectively process large data,
(2) rapidly evaluate population structure, (3) efficiently estimate
variance components several algorithms, (4) implement parallel-accelerated
association tests of markers three methods, (5) globally efficient design
on GWAS process computing, (6) enhance visualization of related
information. 'rMVP' contains three models GLM (Alkes Price (2006)
<DOI:10.1038/ng1847>), MLM (Jianming Yu (2006) <DOI:10.1038/ng1702>) and
FarmCPU (Xiaolei Liu (2016) <doi:10.1371/journal.pgen.1005767>); variance
components estimation methods EMMAX (Hyunmin Kang (2008)
<DOI:10.1534/genetics.107.080101>;), FaSTLMM (method: Christoph Lippert
(2011) <DOI:10.1038/nmeth.1681>, R implementation from 'GAPIT2': You Tang
and Xiaolei Liu (2016) <DOI:10.1371/journal.pone.0107684> and 'SUPER':
Qishan Wang and Feng Tian (2014) <DOI:10.1371/journal.pone.0107684>), and
HE regression (Xiang Zhou (2017) <DOI:10.1214/17-AOAS1052>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
