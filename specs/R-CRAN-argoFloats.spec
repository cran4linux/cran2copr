%global __brp_check_rpaths %{nil}
%global packname  argoFloats
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Oceanographic Argo Floats

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-oce >= 1.3.0
BuildRequires:    R-methods 
Requires:         R-CRAN-oce >= 1.3.0
Requires:         R-methods 

%description
Supports the analysis of oceanographic data recorded by Argo autonomous
drifting profiling floats. Functions are provided to (a) download and
cache data files, (b) subset data in various ways, (c) handle
quality-control flags and (d) plot the results according to oceanographic
conventions. A shiny app is provided for easy exploration of datasets. The
package is designed to work well with the 'oce' package, providing a wide
range of processing capabilities that are particular to oceanographic
analysis. See Kelley, Harbin, and Richards (2021)
<doi:10.3389/fmars.2021.635922> for more on the scientific context and
applications.

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
