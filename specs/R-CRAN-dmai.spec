%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dmai
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Divisia Monetary Aggregates Index

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-utils 

%description
Builds monetary aggregates from their components by the methods of index
number theory. The Divisia index of Barnett (1980)
<doi:10.1016/0304-4076(80)90070-6> weights every component (currency,
demand deposits, savings and time deposits, ...) by its share in the
expenditure on monetary services, priced by its user cost (Barnett 1978)
<doi:10.1016/0165-1765(78)90051-4>. Also gives the Fisher ideal index, a
variant with simple growth rates, the simple-sum aggregate, the currency
equivalent index of Rotemberg, Driscoll and Poterba (1995), the dual
user-cost price index and the Divisia second moments of Barnett and
Serletis (1990) <doi:10.1016/0304-4076(90)90104-2>; benchmark rates given
or taken from the components (upper envelope); 'ggplot2' graphics, a
plain-language interpretation of every result and a built-in 'shiny'
application.

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
