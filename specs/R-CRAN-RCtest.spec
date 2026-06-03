%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RCtest
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reality Check and Predictive Ability Tests for Forecast Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Implements a comprehensive suite of statistical tests for evaluating the
accuracy of forecasting models against a benchmark. The package is
grounded in the reality check framework of White (2000)
<doi:10.1111/1468-0262.00152>, extended by Hansen (2005)
<doi:10.1198/073500105000000063> for Superior Predictive Ability (SPA),
'Giacomini' & White (2006) <doi:10.1111/j.1468-0262.2006.00718.x> for
Conditional Predictive Ability (CPA), and 'Corradi' & Swanson (2006)
<doi:10.1016/j.jeconom.2005.07.026> for predictive density evaluation via
the 'Kullback'-'Leibler' Information Criterion ('KLIC') and 'ZP' Quantile
Loss test, the Continuous Ranked Probability Score ('CRPS') ('Gneiting' &
'Raftery', 2007) <doi:10.1198/016214506000001437>, coverage tests
('Kupiec', 1995) <doi:10.3905/jod.1995.407942>, 'HAC' covariance
estimation ('Newey' & West, 1987) <doi:10.2307/1913610>, and Moving Block
Bootstrap resampling ('Kunsch', 1989) <doi:10.1214/aos/1176347265>.

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
