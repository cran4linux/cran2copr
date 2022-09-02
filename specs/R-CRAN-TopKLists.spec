%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TopKLists
%global packver   1.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Inference, Aggregation and Visualization for Top-K Ranked Lists

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gplots 
Requires:         R-CRAN-Hmisc 
Requires:         R-grid 
Requires:         R-CRAN-gplots 

%description
For multiple ranked input lists (full or partial) representing the same
set of N objects, the package 'TopKLists' <doi:10.1515/sagmb-2014-0093>
offers (1) statistical inference on the lengths of informative top-k
lists, (2) stochastic aggregation of full or partial lists, and (3)
graphical tools for the statistical exploration of input lists, and for
the visualization of aggregation results. Note that RGtk2 and
gWidgets2RGtk2 have been archived on CRAN. See
<https://github.com/pievos101/TopKLists> for installation instructions.

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
