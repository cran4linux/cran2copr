%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  diemr
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Genome Polarization via Diagnostic Index Expectation Maximization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-vcfR 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-circlize 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-vcfR 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-circlize 

%description
Implements a likelihood-based method for genome polarization, identifying
which alleles of SNV markers belong to either side of a barrier to gene
flow. The approach co-estimates individual assignment, barrier strength,
and divergence between sides, with direct application to studies of
hybridization. Includes VCF-to-diem conversion and input checks, support
for mixed ploidy and parallelization, and tools for visualization and
diagnostic outputs. Based on diagnostic index expectation maximization as
described in Baird et al. (2023) <doi:10.1111/2041-210X.14010>.

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
