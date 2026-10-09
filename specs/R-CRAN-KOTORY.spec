%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KOTORY
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Three-Group Tests for Heteroscedasticity in Linear Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-stats 
Requires:         R-CRAN-robustbase 
Requires:         R-stats 

%description
Tests for heteroscedasticity in the linear regression model that sort the
data by a regressor, split them into three equal parts and compare the
error scale of the parts. The ordinary least squares version 'kah3.test()'
refers the ratio of the largest to the smallest residual mean square to
its exact null distribution, Hartley's maximum F-ratio with three groups;
the robust version 'kah.robust.test()' replaces the mean squares by least
trimmed squares scales, so that outliers neither create nor hide
heteroscedasticity, and refers the ratio to a maximum F-ratio with
simulated effective degrees of freedom, to a Monte Carlo reference or to a
residual bootstrap. The distribution, density, quantile and random
generation functions of the maximum F-ratio are provided, together with
'run.all.het()', which runs the proposed tests next to the
Goldfeld-Quandt, Breusch-Pagan, White and robust modified Goldfeld-Quandt
tests in one call. For more details see Hartley (1950)
<doi:10.1093/biomet/37.3-4.308>, Goldfeld and Quandt (1965)
<doi:10.1080/01621459.1965.10480811> and Rousseeuw (1984)
<doi:10.1080/01621459.1984.10477105>.

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
