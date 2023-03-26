%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TapeS
%global packver   0.12.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tree Taper Curves and Sorting Based on 'TapeR'

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-TapeR >= 0.5.2
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-TapeR >= 0.5.2
Requires:         R-methods 
Requires:         R-utils 

%description
Providing new german-wide 'TapeR' Models and functions for their
evaluation. Included are the most common tree species in Germany (Norway
spruce, Scots pine, European larch, Douglas fir, Silver fir as well as
European beech, Common/Sessile oak and Red oak). Many other species are
mapped to them so that 36 tree species / groups can be processed. Single
trees are defined by species code, one or multiple diameters in arbitrary
measuring height and tree height. The functions then provide information
on diameters along the stem, bark thickness, height of diameters, volume
of the total or parts of the trunk and total and component above-ground
biomass. It is also possible to calculate assortments from the taper
curves. For diameter and volume estimation, uncertainty information is
given.

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
