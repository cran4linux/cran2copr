%global packname  spcosa
%global packver   0.3-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.11
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Coverage Sampling and Random Sampling from Compact Geographical Strata

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal >= 1.5.19
BuildRequires:    R-CRAN-sp >= 1.1.0
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-rJava >= 0.9.3
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-rgdal >= 1.5.19
Requires:         R-CRAN-sp >= 1.1.0
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-rJava >= 0.9.3
Requires:         R-methods 
Requires:         R-utils 

%description
Spatial coverage sampling and random sampling from compact geographical
strata created by k-means. See Walvoort et al. (2010)
<doi:10.1016/j.cageo.2010.04.005> for details.

%prep
%setup -q -c -n %{packname}
sed -i '/Sexpr/d' %{packname}/man/spcosa-package.Rd
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
