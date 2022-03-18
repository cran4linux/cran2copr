%global __brp_check_rpaths %{nil}
%global packname  dQTG.seq
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A BSA Software for Detecting All Types of QTLs in BC, DH, RIL and F2

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-writexl 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
The new (dQTG.seq1 and dQTG.seq2) and existing (SmoothLOD, G', deltaSNP
and ED) bulked segregant analysis methods are used to identify various
types of quantitative trait loci for complex traits via extreme phenotype
individuals in bi-parental segregation populations (F2, backcross, doubled
haploid and recombinant inbred line). The numbers of marker alleles in
extreme low and high pools are used in existing methods to identify
trait-related genes, while the numbers of marker alleles and genotypes in
extreme low and high pools are used in the new methods to construct a new
statistic Gw for identifying trait-related genes. dQTG-seq2 is feasible to
identify extremely over-dominant and small-effect genes in F2.

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
