%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  methFuse
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Segmentation of the Methylome

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-methods 

%description
Implements FUSE (Functional Segmentation of DNA methylation data), a
data-driven method for identifying spatially coherent DNA methylation
segments from whole-genome bisulfite sequencing (WGBS) count data. The
method performs hierarchical clustering of CpG sites based on methylated
and unmethylated read counts across multiple samples and determines the
optimal number of segments using an information criterion (AIC or BIC).
Resulting segments represent regions with homogeneous methylation profiles
across the input cohort while allowing sample-specific methylation levels.
The package provides functions for clustering, model selection, tree
cutting, segment-level summarization, and visualization. Input can be
supplied as count matrices or extracted directly from 'BSseq' and
'methrix' objects.

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
