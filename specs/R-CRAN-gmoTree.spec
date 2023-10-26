%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gmoTree
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Get and Modify 'oTree' Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.3.0
BuildRequires:    R-CRAN-openxlsx >= 4.2.5.2
BuildRequires:    R-CRAN-plyr >= 1.8.8
BuildRequires:    R-CRAN-stringr >= 1.5.0
BuildRequires:    R-CRAN-data.table >= 1.14.8
BuildRequires:    R-CRAN-dplyr >= 1.1.2
BuildRequires:    R-CRAN-rlang >= 1.1.1
BuildRequires:    R-CRAN-rlist >= 0.4.6.2
Requires:         R-stats >= 4.3.0
Requires:         R-CRAN-openxlsx >= 4.2.5.2
Requires:         R-CRAN-plyr >= 1.8.8
Requires:         R-CRAN-stringr >= 1.5.0
Requires:         R-CRAN-data.table >= 1.14.8
Requires:         R-CRAN-dplyr >= 1.1.2
Requires:         R-CRAN-rlang >= 1.1.1
Requires:         R-CRAN-rlist >= 0.4.6.2

%description
Manage data from 'oTree' experiments.  Import 'oTree' data and clean them
up by using functions to deal with messy data, dropouts, and other
problematic cases. Create IDs, calculate the time, transfer variables
between app data frames, and delete sensitive information. You can also
check your experimental data before running the experiment. Information on
'oTree' is found in Chen, D. L., Schonger, M., & Wickens, C. (2016) <doi:
10.1016/j.jbef.2015.12.001>.

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
