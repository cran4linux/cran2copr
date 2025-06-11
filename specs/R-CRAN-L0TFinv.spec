%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  L0TFinv
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Splicing Approach to the Inverse Problem of L0 Trend Filtering

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 

%description
Trend filtering is a widely used nonparametric method for knot detection.
This package provides an efficient solution for L0 trend filtering,
avoiding the traditional methods of using Lagrange duality or Alternating
Direction Method of Multipliers algorithms. It employ a splicing approach
that minimizes L0-regularized sparse approximation by transforming the L0
trend filtering problem. The package excels in both efficiency and
accuracy of trend estimation and changepoint detection in segmented
functions. References: Wen et al. (2020) <doi:10.18637/jss.v094.i04>; Zhu
et al. (2020)<doi:10.1073/pnas.2014241117>; Wen et al. (2023)
<doi:10.1287/ijoc.2021.0313>.

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
