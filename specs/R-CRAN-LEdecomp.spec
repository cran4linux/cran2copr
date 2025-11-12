%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LEdecomp
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Decompose Life Expectancy by Age (and Cause)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3
Requires:         R-core >= 4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-DemoDecomp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-DemoDecomp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 

%description
A set of all-cause and cause-specific life expectancy sensitivity and
decomposition methods, including Arriaga (1984) <doi:10.2307/2061029>,
others documented by Ponnapalli (2005) <doi:10.4054/DemRes.2005.12.7>,
lifetable, numerical, and other algorithmic approaches such as Horiuchi et
al (2008) <doi:10.1353/dem.0.0033>, or Andreev et al (2002)
<doi:10.4054/DemRes.2002.7.14>.

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
