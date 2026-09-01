%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ruv
%global packver   0.9.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Detect and Remove Unwanted Variation using Negative Controls

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-gridExtra 

%description
Implements the 'RUV' (Remove Unwanted Variation) algorithms.  These
algorithms attempt to adjust for systematic errors of unknown origin in
high-dimensional data.  The algorithms were originally developed for use
with genomic data, especially microarray data, but may be useful with
other types of high-dimensional data as well.  These algorithms were
proposed in Gagnon-Bartsch and Speed (2012) <doi:10.1093/nar/gkz433>,
Gagnon-Bartsch, Jacob and Speed (2013), and Molania, et. al. (2019)
<doi:10.1093/nar/gkz433>.  The algorithms require the user to specify a
set of negative control variables, as described in the references.  The
algorithms included in this package are 'RUV-2', 'RUV-4', 'RUV-inv',
'RUV-rinv', 'RUV-I', and RUV-III', along with various supporting
algorithms.

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
