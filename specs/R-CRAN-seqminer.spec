%global __brp_check_rpaths %{nil}
%global packname  seqminer
%global packver   8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.2
Release:          1%{?dist}%{?buildtag}
Summary:          Efficiently Read Sequence Data (VCF Format, BCF Format, METAL Format and BGEN Format) into R

License:          GPL | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zlib-devel
BuildRequires:    R-devel
Requires:         R-core

%description
Integrate sequencing data (Variant call format, e.g. VCF or BCF) or
meta-analysis results in R. This package can help you (1) read
VCF/BCF/BGEN files by chromosomal ranges (e.g. 1:100-200); (2) read
RareMETAL summary statistics files; (3) read tables from a tabix-indexed
files; (4) annotate VCF/BCF files; (5) create customized workflow based on
Makefile.

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
