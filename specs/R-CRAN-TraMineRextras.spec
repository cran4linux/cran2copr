%global __brp_check_rpaths %{nil}
%global packname  TraMineRextras
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          TraMineR Extension

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-TraMineR >= 2.2.1
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-TraMineR >= 2.2.1
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Collection of ancillary functions and utilities to be used in conjunction
with the 'TraMineR' package for sequence data exploration. Includes, among
others, specific functions such as state survival plots, position-wise
group-typical states, dynamic sequence indicators, and dissimilarities
between event sequences. Also includes contributions by non-members of the
TraMineR team such as the relative frequency plot and methods for polyadic
data.

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
