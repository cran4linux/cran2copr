%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HistogramTools
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Functions for R Histograms

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ash 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-ash 
Requires:         R-CRAN-Hmisc 

%description
Provides a number of utility functions useful for manipulating large
histograms.  This includes methods to trim, subset, merge buckets, merge
histograms, convert to CDF, and calculate information loss due to binning.
It also provides a protocol buffer representation of R's native histogram
class to allow histograms over large data sets to be computed and combined
in distributed analytical pipelines.  Implements bin-by-bin histogram
distance measures described in Rubner, Tomasi and Guibas (2000)
<doi:10.1023/A:1026543900054>, Swain and Ballard (1991)
<doi:10.1007/BF00130487>, and Puzicha, Hofmann and Buhmann (1997)
<doi:10.1109/CVPR.1997.609331>, and average shifted histograms as in Scott
(2015, ISBN:9781118575536).

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
