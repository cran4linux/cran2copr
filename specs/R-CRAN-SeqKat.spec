%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SeqKat
%global packver   0.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Detection of Kataegis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Kataegis is a localized hypermutation occurring when a region is enriched
in somatic SNVs. Kataegis can result from multiple cytosine deaminations
catalyzed by the AID/APOBEC family of proteins. This package contains
functions to detect kataegis from SNVs in BED format. This package reports
two scores per kataegic event, a hypermutation score and an APOBEC
mediated kataegic score. Yousif, F. et al.; The Origins and Consequences
of Localized and Global Somatic Hypermutation; Biorxiv 2018
<doi:10.1101/287839>.

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
