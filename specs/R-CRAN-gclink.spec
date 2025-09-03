%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gclink
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Gene-Cluster Discovery, Annotation and Visualization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-gggenes >= 0.5.1
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-gggenes >= 0.5.1
Requires:         R-utils 

%description
Performs end-to-end analysis of gene clusters—such as photosynthesis,
carbon/nitrogen/sulfur cycling, carotenoid, antibiotic, or viral marker
genes (e.g., capsid, polymerase, integrase)—from genomes and metagenomes.
It parses Basic Local Alignment Search Tool (BLAST) results in
tab-delimited format produced by tools like NCBI BLAST+ and Diamond
BLASTp, filters Open Reading Frames (ORFs) by length, detects contiguous
clusters of reference genes, optionally extracts genomic coordinates,
merges functional annotations, and generates publication-ready arrow
plots. The package works seamlessly with or without the coding sequences
input and skips plotting when no functional groups are found. For more
details see Li et al. (2023) <doi:10.1038/s41467-023-42193-7>.

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
