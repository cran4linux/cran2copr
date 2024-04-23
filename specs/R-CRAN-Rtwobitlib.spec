%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rtwobitlib
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}%{?buildtag}
Summary:          '2bit' 'C' Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-tools 
Requires:         R-tools 

%description
A trimmed down copy of the "kent-core source tree" turned into a 'C'
library for manipulation of '.2bit' files. See
<https://genome.ucsc.edu/FAQ/FAQformat.html#format7> for a quick overview
of the '2bit' format. The "kent-core source tree" can be found here:
<https://github.com/ucscGenomeBrowser/kent-core/>. Only the '.c' and '.h'
files from the source tree that are related to manipulation of '.2bit'
files were kept. Note that the package is primarily useful to developers
of other R packages who wish to use the '2bit' 'C' library in their own
'C'/'C++' code.

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
