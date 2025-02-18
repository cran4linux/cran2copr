%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gmoTree
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Get and Modify 'oTree' Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2.5.2
BuildRequires:    R-CRAN-rmarkdown >= 2.27
BuildRequires:    R-CRAN-plyr >= 1.8.9
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-knitr >= 1.47
BuildRequires:    R-CRAN-data.table >= 1.15.4
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-lifecycle >= 1.0.4
BuildRequires:    R-CRAN-pander >= 0.6.5
BuildRequires:    R-CRAN-rlist >= 0.4.6.2
Requires:         R-CRAN-openxlsx >= 4.2.5.2
Requires:         R-CRAN-rmarkdown >= 2.27
Requires:         R-CRAN-plyr >= 1.8.9
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-knitr >= 1.47
Requires:         R-CRAN-data.table >= 1.15.4
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-lifecycle >= 1.0.4
Requires:         R-CRAN-pander >= 0.6.5
Requires:         R-CRAN-rlist >= 0.4.6.2

%description
Efficiently manage and process data from 'oTree' experiments. Import
'oTree' data and clean them by using functions that handle messy data,
dropouts, and other problematic cases.  Create IDs, calculate the time,
transfer variables between app data frames, and delete sensitive
information.  Review your experimental data prior to running the
experiment and automatically generate a detailed summary of the variables
used in your 'oTree' code.  Information on 'oTree' is found in Chen, D.
L., Schonger, M., & Wickens, C. (2016) <doi:10.1016/j.jbef.2015.12.001>.

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
