%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSplots
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Stock Status Plots (SSPs)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-zoo 

%description
Pauly et al. (2008)
<http://legacy.seaaroundus.s3.amazonaws.com/doc/Researcher+Publications/dpauly/PDF/2008/Books%%26Chapters/FisheriesInLargeMarineEcosystems.pdf>
created (and coined the name) 'Stock Status Plots' for a UNEP compendium
on Large Marine Ecosystems (LMEs, Sherman and Hempel 2008
<https://agris.fao.org/agris-search/search.do?recordID=XF2015036057>).
Stock status plots are bivariate graphs summarizing the status (e.g.,
developing, fully exploited, overexploited, etc.), through time, of the
multispecies fisheries of a fished area or ecosystem. This package
contains two functions to generate stock status plots viz.,
SSplots_pauly() (as per the criteria proposed by Pauly et al.,2008) and
SSplots_kleisner() (as per the criteria proposed by Kleisner and Pauly
(2011) <http://www.ecomarres.com/downloads/regional.pdf> and Kleisner et
al. (2013) <doi:10.1111/j.1467-2979.2012.00469.x>).

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
