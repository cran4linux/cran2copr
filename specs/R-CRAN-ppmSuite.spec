%global packname  ppmSuite
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Models that Employ a Prior Distribution on Partitions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
Provides functions that fit hierarchical Gaussian and probit ordinal
models. A (covariate dependent) product partition model is used as a
prior. If a covariate dependent product partition model is selected, then
all the options detailed in Page, G.L.; Quintana, F.A.; (2018)
<doi:10.1007/s11222-017-9777-z> are available.  If covariate values are
missing, then the approach detailed in Page, G.L.; Quintana, F.A.;
Mueller, P (2020) <arXiv:1912.13119> is employed.  Also included in the
package is a function that fits a Gaussian likelihood spatial product
partition model that is detailed in Page, G.L.; Quintana, F.A.; (2016)
<doi:10.1214/15-BA971>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
