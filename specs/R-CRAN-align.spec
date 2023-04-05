%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  align
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Modified DTW Algorithm for Stratigraphic Time Series Alignment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-stats 
Requires:         R-CRAN-matlab 
Requires:         R-stats 

%description
A dynamic time warping (DTW) algorithm for stratigraphic alignment,
translated into R from the original published 'MATLAB' code by Hay et al.
(2019) <doi:10.1130/G46019.1>. The DTW algorithm incorporates two
geologically relevant parameters (g and edge) for augmenting the typical
DTW cost matrix, allowing for a range of sedimentologic and chronologic
conditions to be explored, as well as the generation of an alignment
library (as opposed to a single alignment solution). The g parameter
relates to the relative sediment accumulation rate between the two time
series records, while the edge parameter relates to the amount of total
shared time between the records. Note that this algorithm is used for all
DTW alignments in the Align Shiny application, detailed in Hagen et al.
(in review).

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
