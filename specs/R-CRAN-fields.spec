%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fields
%global packver   16.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          16.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Spatial Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-maps 
Requires:         R-methods 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-maps 

%description
For curve, surface and function fitting with an emphasis on splines,
spatial data, geostatistics, and spatial statistics. The major methods
include cubic, and thin plate splines, Kriging, and compactly supported
covariance functions for large data sets. The splines and Kriging methods
are supported by functions that can determine the smoothing parameter
(nugget and sill variance) and other covariance function parameters by
cross validation and also by restricted maximum likelihood. For Kriging
there is an easy to use function that also estimates the correlation scale
(range parameter).  A major feature is that any covariance function
implemented in R and following a simple format can be used for spatial
prediction. There are also many useful functions for plotting and working
with spatial data as images. This package also contains an implementation
of sparse matrix methods for large spatial data sets and currently
requires the sparse matrix (spam) package. Use help(fields) to get started
and for an overview.  The fields source code is deliberately commented and
provides useful explanations of numerical details as a companion to the
manual pages. The commented source code can be viewed by expanding the
source code version and looking in the R subdirectory. The reference for
fields can be generated by the citation function in R and has DOI
<doi:10.5065/D6W957CT>. Development of this package was supported in part
by the National Science Foundation Grant 1417857, the National Center for
Atmospheric Research, and Colorado School of Mines. See the Fields URL for
a vignette on using this package and some background on spatial
statistics.

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
