%global __brp_check_rpaths %{nil}
%global packname  estudy2
%global packver   0.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          1%{?dist}%{?buildtag}
Summary:          An Implementation of Parametric and Nonparametric Event Study

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-curl >= 4.3.2
BuildRequires:    R-CRAN-zoo >= 1.8.9
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-matrixStats >= 0.60.0
BuildRequires:    R-CRAN-quantmod >= 0.4.18
Requires:         R-CRAN-curl >= 4.3.2
Requires:         R-CRAN-zoo >= 1.8.9
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-matrixStats >= 0.60.0
Requires:         R-CRAN-quantmod >= 0.4.18

%description
An implementation of a most commonly used event study methodology,
including both parametric and nonparametric tests. It contains variety
aspects of the rate of return estimation (the core calculation is done in
C++), as well as three classical for event study market models: mean
adjusted returns, market adjusted returns and single-index market models.
There are 6 parametric and 6 nonparametric tests provided, which examine
cross-sectional daily abnormal return (see the documentation of the
functions for more information). Parametric tests include tests proposed
by Brown and Warner (1980) <DOI:10.1016/0304-405X(80)90002-1>, Brown and
Warner (1985) <DOI:10.1016/0304-405X(85)90042-X>, Boehmer et al. (1991)
<DOI:10.1016/0304-405X(91)90032-F>, Patell (1976) <DOI:10.2307/2490543>,
and Lamb (1995) <DOI:10.2307/253695>. Nonparametric tests covered in
estudy2 are tests described in Corrado and Zivney (1992)
<DOI:10.2307/2331331>, McConnell and Muscarella (1985)
<DOI:10.1016/0304-405X(85)90006-6>, Boehmer et al. (1991)
<DOI:10.1016/0304-405X(91)90032-F>, Cowan (1992) <DOI:10.1007/BF00939016>,
Corrado (1989) <DOI:10.1016/0304-405X(89)90064-0>, Campbell and Wasley
(1993) <DOI:10.1016/0304-405X(93)90025-7>, Savickas (2003)
<DOI:10.1111/1475-6803.00052>, Kolari and Pynnonen (2010)
<DOI:10.1093/rfs/hhq072>. Furthermore, tests for the cumulative abnormal
returns proposed by Brown and Warner (1985)
<DOI:10.1016/0304-405X(85)90042-X> and Lamb (1995) <DOI:10.2307/253695>
are included.

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
