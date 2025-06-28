%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CooccurrenceAffinity
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Affinity in Co-Occurrence Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-BiasedUrn >= 2.0.9
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape 
Requires:         R-CRAN-BiasedUrn >= 2.0.9
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape 

%description
Computes a novel metric of affinity between two entities based on their
co-occurrence (using binary presence/absence data). The metric and its
MLE, alpha hat, were advanced in Mainali, Slud, et al, 2021
<doi:10.1126/sciadv.abj9204>. Various types of confidence intervals and
median interval were developed in Mainali and Slud, 2022
<doi:10.1101/2022.11.01.514801>. The `finches` dataset is now bundled
internally (no longer pulled via the cooccur package, which has been
dropped).

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
