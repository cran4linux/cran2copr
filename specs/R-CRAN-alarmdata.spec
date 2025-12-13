%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  alarmdata
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Download, Merge, and Process Redistricting Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-redist >= 4.2.0
BuildRequires:    R-CRAN-geomander >= 2.1.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dataverse 
BuildRequires:    R-CRAN-censable 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-redistmetrics 
BuildRequires:    R-CRAN-tinytiger 
BuildRequires:    R-CRAN-rappdirs 
Requires:         R-CRAN-redist >= 4.2.0
Requires:         R-CRAN-geomander >= 2.1.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dataverse 
Requires:         R-CRAN-censable 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-redistmetrics 
Requires:         R-CRAN-tinytiger 
Requires:         R-CRAN-rappdirs 

%description
Utility functions to download and process data produced by the ALARM
Project, including 2020 redistricting files Kenny and McCartan (2021)
<https://alarm-redist.org/posts/2021-08-10-census-2020/> and the 50-State
Redistricting Simulations of McCartan, Kenny, Simko, Garcia, Wang, Wu,
Kuriwaki, and Imai (2022) <doi:10.7910/DVN/SLCD3E>. The package extends
the data introduced in McCartan, Kenny, Simko, Garcia, Wang, Wu, Kuriwaki,
and Imai (2022) <doi:10.1038/s41597-022-01808-2> to also include states
with only a single district. The package also includes the Japanese 2022
redistricting files from the 47-Prefecture Redistricting Simulations of
Miyazaki, Yamada, Yatsuhashi, and Imai (2022) <doi:10.7910/DVN/Z9UKSH>.

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
