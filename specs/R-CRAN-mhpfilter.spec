%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mhpfilter
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modified and Fully Modified Hodrick-Prescott Filters

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Decomposes macroeconomic time series into trend and cycle with the
Hodrick-Prescott (HP) filter and two data-driven versions of it. The
modified HP filter of McDermott (1997), assessed by Choudhary, Hanif and
Iqbal (2014) <doi:10.1080/00036846.2014.894631>, chooses the smoothing
parameter of every series by generalised cross-validation (as described in
Coe and McDermott (1997) <doi:10.2307/3867497>). The fully modified HP
filter of Hanif, Iqbal and Choudhary (2017, State Bank of Pakistan Working
Paper 88) also reduces the end-point bias of the HP filter: it raises the
smoothing parameter at the first and last observations, with linear or
quadratic weights chosen to minimise the loss of Bloechl (2014, University
of Munich Discussion Paper 2014-1). Every filter is a banded linear solve,
so the searches are fast; batch processing of many series, comparisons of
the filters, the filter weights, gain functions and end-point loss,
simulation of trend-plus-cycle series and the power comparison of the
paper, 'ggplot2' graphics, a plain-language interpretation of every result
and a built-in 'shiny' application.

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
