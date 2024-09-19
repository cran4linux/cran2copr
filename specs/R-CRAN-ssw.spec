%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssw
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Striped Smith-Waterman Algorithm for Sequence Alignment using SIMD

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-reticulate 

%description
Provides an R interface for 'SSW' (Striped Smith-Waterman) via its
'Python' binding 'ssw-py'. 'SSW' is a fast 'C' and 'C++' implementation of
the Smith-Waterman algorithm for pairwise sequence alignment using
Single-Instruction-Multiple-Data (SIMD) instructions. 'SSW' enhances the
standard algorithm by efficiently returning alignment information and
suboptimal alignment scores. The core 'SSW' library offers performance
improvements for various bioinformatics tasks, including protein database
searches, short-read alignments, primary and split-read mapping,
structural variant detection, and read-overlap graph generation. These
features make 'SSW' particularly useful for genomic applications. Zhao et
al. (2013) <doi:10.1371/journal.pone.0082138> developed the original 'C'
and 'C++' implementation.

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
