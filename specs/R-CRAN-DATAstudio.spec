%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DATAstudio
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          The Research Data Warehouse of Miguel de Carvalho

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Pulls together a collection of datasets from Miguel de Carvalho research
articles. Including, for example: - de Carvalho (2012)
<doi:10.1016/j.jspi.2011.08.016>; - de Carvalho et al (2012)
<doi:10.1080/03610926.2012.709905>; - de Carvalho et al (2012)
<doi:10.1016/j.econlet.2011.09.007>); - de Carvalho and Davison (2014)
<doi:10.1080/01621459.2013.872651>; - de Carvalho and Rua (2017)
<doi:10.1016/j.ijforecast.2015.09.004>; - de Carvalho et al (2023)
<doi:10.1002/sta4.560>; - de Carvalho et al (2022)
<doi:10.1007/s13253-021-00469-9>; - Palacios et al (2024)
<doi:10.1214/24-BA1420>.

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
