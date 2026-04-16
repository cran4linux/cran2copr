%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GFFStrandLoc
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Strand-Wise Gene and Protein Extraction from GFF3 Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Facilitates the extraction and organization of strand-specific genomic
features from GFF3 files. In many species and variants, high quality
genome annotations are not always available, necessitating de novo
annotation using tools such as AUGUSTUS (Stanke et al., 2006;
<doi:10.1093/nar/gkl200>). However, downstream processing of such
annotations to obtain structured information, such as strand-wise gene
locations, transcript regions, and associated protein identifiers—can be
computationally intensive and complex. 'GFFStrandLoc' provides a
streamlined framework to parse GFF3 files and generate structured outputs
containing strand-wise and region-wise genomic coordinates for each
transcript, along with their associated protein information. Additionally,
it enables users to define custom promoter lengths and extract
corresponding promoter region coordinates for genes in a strand-aware
manner. By simplifying post-annotation processing, it enhances the
usability of de novo annotated genomic datasets for downstream analysis
and interpretation.

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
