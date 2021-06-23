%global __brp_check_rpaths %{nil}
%global packname  wrMisc
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze Experimental High-Throughput (Omics) Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
The efficient treatment and convenient analysis of experimental
high-throughput (omics) data gets facilitated through this collection of
diverse functions. Several functions address advanced object-conversions,
like manipulating lists of lists or lists of arrays, reorganizing lists to
arrays or into separate vectors, merging of multiple entries, etc. Another
set of functions provides speed-optimized calculation of standard
deviation (sd), coefficient of variance (CV) or standard error of the mean
(SEM) for data in matrixes or means per line with respect to additional
grouping (eg n groups of replicates). Other functions facilitate dealing
with non-redundant information, by indexing unique, adding counters to
redundant or eliminating lines with respect redundancy in a given
reference-column, etc. Help is provided to identify very closely matching
numeric values to generate (partial) distance matrixes for very big data
in a memory efficient manner or to reduce the complexity of large
data-sets by combining very close values. Many times large experimental
datasets need some additional filtering, adequate functions are provided.
Batch reading (or writing) of sets of files and combining data to arrays
is supported, too. Convenient data normalization is supported in various
different modes, parameter estimation via permutations or boot-strap as
well as flexible testing of multiple pair-wise combinations using the
framework of 'limma' is provided, too.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
