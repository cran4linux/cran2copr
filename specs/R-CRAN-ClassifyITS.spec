%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ClassifyITS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fungal Assignment Pipeline

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-seqinr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-seqinr 

%description
Fungi are ubiquitous in Earth's wonderfully diverse ecosystems. The
'ClassifyITS' package aids in the taxonomic classification of
environmental internal transcribed spacer (ITS) short-read barcoding data.
Unlike previous methods, it employs taxon-specific e-value and percent
identity cutoffs at each taxonomic rank from kingdom to species. The
package takes a conservative approach and outputs both graphics and
user-friendly files to help users manually inspect fungal operational
taxonomic units (OTUs) that fail classification at relevant levels (e.g.,
Phylum). 'ClassifyITS' is based on taxonomic cutoff criteria from "The
Global Soil Mycobiome consortium dataset for boosting fungal diversity
research" (Fungal Diversity, Tedersoo, 2021,
<doi:10.1007/s13225-021-00493-7>) and "Best practices in metabarcoding of
fungi: From experimental design to results" (Molecular Ecology, Tedersoo,
2022, <doi:10.1111/mec.16460>).

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
