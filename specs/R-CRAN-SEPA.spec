%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SEPA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Segment Profile Extraction via Pattern Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot >= 1.3.28
BuildRequires:    R-parallel 
Requires:         R-CRAN-boot >= 1.3.28
Requires:         R-parallel 

%description
Implements the Segment Profile Extraction via Pattern Analysis method for
row-mean-centered multivariate data. Core capabilities include SVD-based
row-isometric biplot construction, bias-corrected and accelerated, and
percentile bootstrap confidence intervals for domain coordinates and
per-person direction cosines, Procrustes alignment of bootstrap replicates
across planes, parallel analysis for dimensionality selection, and segment
profile reconstruction in planes defined by pairs of singular dimensions.
A synthetic Woodcock-Johnson IV look-alike dataset is provided for
examples and testing. The method is described in Kim and Grochowalski
(2019) <doi:10.1007/s00357-018-9277-7>.

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
