%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  npwbs
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Multiple Change Point Detection Using Wild Binary Segmentation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-Rcpp 

%description
Implements nonparametric multiple change-point detection for univariate
sequences using Wild Binary Segmentation, as described in Ross (2026)
"Nonparametric Detection of Multiple Location-Scale Change Points via Wild
Binary Segmentation" <doi:10.48550/arXiv.2107.01742>. The package provides
Mann--Whitney, Mood, Lepage, Cramér--von Mises, modified Baumgartner, and
standardised Zhang Z_C rank-based statistics, together with
method-specific thresholds for controlling the probability of incorrectly
detecting a change point in a homogeneous sequence.

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
