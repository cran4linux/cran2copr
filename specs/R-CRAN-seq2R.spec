%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seq2R
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Method to Detect Compositional Changes in Genomic Sequences

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-seqinr 
Requires:         R-CRAN-seqinr 

%description
This software is useful for loading '.fasta' or '.gbk' files, and for
retrieving sequences from 'GenBank' dataset
<https://www.ncbi.nlm.nih.gov/genbank/>. This package allows to detect
differences or asymmetries based on nucleotide composition by using local
linear kernel smoothers. Also, it is possible to draw inference about
critical points (i. e. maximum or minimum points) related with the
derivative curves. Additionally, bootstrap methods have been used for
estimating confidence intervals and speed computational techniques
(binning techniques) have been implemented in 'seq2R'.

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
