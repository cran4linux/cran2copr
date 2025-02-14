%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fitPoly
%global packver   4.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Genotype Calling for Bi-Allelic Marker Assays

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-devEMF 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-devEMF 
Requires:         R-CRAN-doParallel 
Requires:         R-grDevices 

%description
Genotyping assays for bi-allelic markers (e.g. SNPs) produce signal
intensities for the two alleles. 'fitPoly' assigns genotypes (allele
dosages) to a collection of polyploid samples based on these signal
intensities. 'fitPoly' replaces the older package 'fitTetra' that was
limited (a.o.) to only tetraploid populations whereas 'fitPoly' accepts
any ploidy level. Reference: Voorrips RE, Gort G, Vosman B (2011)
<doi:10.1186/1471-2105-12-172>. New functions added on conversion of data
from SNP array software formats, drawing of XY-scatterplots with or
without genotype colors, checking against expected F1 segregation
patterns, comparing results from two different assays (probes) for the
same SNP, recovery from a saveMarkerModels() crash.

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
