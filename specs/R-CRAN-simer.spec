%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simer
%global packver   0.9.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Data Simulation for Life Science and Breeding

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-bigmemory 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-igraph 

%description
Data simulator including genotype, phenotype, pedigree, selection and
reproduction in R. It simulates most of reproduction process of animals or
plants and provides data for GS (Genomic Selection), GWAS (Genome-Wide
Association Study), and Breeding. For ADI model, please see Kao C and Zeng
Z (2002) <doi:10.1093/genetics/160.3.1243>. For build.cov, please see B.
D. Ripley (1987) <ISBN:9780470009604>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
