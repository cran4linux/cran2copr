%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shaman
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sampling Hi-C Contact Matrices for Aparametric Normalization

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-misha >= 3.5.6
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-parallel 
Requires:         R-CRAN-misha >= 3.5.6
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-reshape2 
Requires:         R-grid 
Requires:         R-CRAN-plyr 
Requires:         R-parallel 

%description
Generate expected Hi-C (genome-wide chromosome conformation capture) data
maintaining marginal coverage, and the decay in contact probability with
increasing genomic distance. Expected Hi-C data is used for normalization
and graphical presentation of statistical significance of observed Hi-C
contact enrichments. The method is described in Mendelson Cohen et al.
(2017) <doi:10.1101/187203>.

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
