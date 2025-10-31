%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BasketballAnalyzeR
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Visualization of Basketball Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3
BuildRequires:    R-utils >= 4.2.3
BuildRequires:    R-CRAN-statnet.common >= 4.2
BuildRequires:    R-CRAN-gtools >= 3.9.4
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-directlabels >= 2018.05
BuildRequires:    R-CRAN-PBSmapping >= 2.70
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-mathjaxr >= 1.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-GGally >= 1.4
BuildRequires:    R-CRAN-sp >= 1.3
BuildRequires:    R-CRAN-stringr >= 1.3
BuildRequires:    R-CRAN-readr >= 1.3
BuildRequires:    R-CRAN-data.table >= 1.14
BuildRequires:    R-CRAN-corrplot >= 0.80
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-CRAN-ggrepel >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.7.6
BuildRequires:    R-CRAN-rlang >= 0.4.3
BuildRequires:    R-CRAN-operators >= 0.1
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-MASS >= 7.3
Requires:         R-utils >= 4.2.3
Requires:         R-CRAN-statnet.common >= 4.2
Requires:         R-CRAN-gtools >= 3.9.4
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-directlabels >= 2018.05
Requires:         R-CRAN-PBSmapping >= 2.70
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-mathjaxr >= 1.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-GGally >= 1.4
Requires:         R-CRAN-sp >= 1.3
Requires:         R-CRAN-stringr >= 1.3
Requires:         R-CRAN-readr >= 1.3
Requires:         R-CRAN-data.table >= 1.14
Requires:         R-CRAN-corrplot >= 0.80
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-ggrepel >= 0.8
Requires:         R-CRAN-dplyr >= 0.7.6
Requires:         R-CRAN-rlang >= 0.4.3
Requires:         R-CRAN-operators >= 0.1
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Contains data and code to accompany the book P. Zuccolotto and M. Manisera
(2020) Basketball Data Science. Applications with R. CRC Press. ISBN
9781138600799.

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
