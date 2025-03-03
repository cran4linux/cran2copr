%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  popsom7
%global packver   7.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Fast, User-Friendly Implementation of Self-Organizing Maps (SOMs)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-som 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-fields 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hash 
Requires:         R-stats 
Requires:         R-CRAN-som 
Requires:         R-grDevices 

%description
Methods for building self-organizing maps (SOMs) with a number of
distinguishing features such automatic centroid detection and cluster
visualization using starbursts.  For more details see the paper "Improved
Interpretability of the Unified Distance Matrix with Connected Components"
by Hamel and Brown (2011) in <ISBN:1-60132-168-6>.  The package provides
user-friendly access to two models we construct: (a) a SOM model and (b) a
centroid based clustering model. The package also exposes a number of
quality metrics for the quantitative evaluation of the map, Hamel (2016)
<doi:10.1007/978-3-319-28518-4_4>.  Finally, we reintroduced our fast,
vectorized training algorithm for SOM with substantial improvements. It is
about an order of magnitude faster than the canonical, stochastic C
implementation <doi:10.1007/978-3-030-01057-7_60>.

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
