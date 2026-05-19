%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quaqcr
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Quick ATAC-Seq QC

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 

%description
A wrapper around the 'quaqc' program described in Tremblay and Questa
(2024) <doi:10.1093/bioinformatics/btae649>. 'quaqc' allows for assay for
transposase-accessible chromatin using sequencing (ATAC-seq) specific
quality control and read filtering of next-generation sequencing (NGS)
data with minimal processing time and extremely low memory overhead. Any
number of samples can be processed, using multiple threads if desired.
'quaqc' outputs a comprehensive set of aligned read metrics, including
alignment size, fragment size, percent duplicates, mapq scores, read
depth, GC content, and others. Although designed for ATAC-seq data,
'quaqc' can also be used for other unspliced DNA sequencing experiments
(such as chromatin immunoprecipitation sequencing, or ChIP-seq) as many of
the metrics are related to general sequencing quality. This R package also
provides additional utilities for custom analyses and plotting of 'quaqc'
results.

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
