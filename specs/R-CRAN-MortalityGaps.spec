%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MortalityGaps
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          The Double-Gap Life Expectancy Forecasting Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.4
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-CRAN-pbapply >= 1.3
BuildRequires:    R-CRAN-crch >= 1.0
BuildRequires:    R-CRAN-Rdpack >= 0.9.0
Requires:         R-CRAN-forecast >= 8.4
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-CRAN-pbapply >= 1.3
Requires:         R-CRAN-crch >= 1.0
Requires:         R-CRAN-Rdpack >= 0.9.0

%description
Life expectancy is highly correlated over time among countries and between
males and females. These associations can be used to improve forecasts.
Here we have implemented a method for forecasting female life expectancy
based on analysis of the gap between female life expectancy in a country
compared with the record level of female life expectancy in the world.
Second, to forecast male life expectancy, the gap between male life
expectancy and female life expectancy in a country is analysed. We named
this method the Double-Gap model. For a detailed description of the method
see Pascariu et al. (2018). <doi:10.1016/j.insmatheco.2017.09.011>.

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
