%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  anabel
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Binding Events + l

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-openxlsx >= 4.2
BuildRequires:    R-stats >= 4.0
BuildRequires:    R-utils >= 4.0
BuildRequires:    R-CRAN-cli >= 3.4
BuildRequires:    R-CRAN-ggplot2 >= 3.3
BuildRequires:    R-CRAN-reshape2 >= 1.4
BuildRequires:    R-CRAN-kableExtra >= 1.3
BuildRequires:    R-CRAN-minpack.lm >= 1.2
BuildRequires:    R-CRAN-progress >= 1.2
BuildRequires:    R-CRAN-tidyr >= 1.2
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-rlang >= 1.0
BuildRequires:    R-CRAN-purrr >= 0.3
BuildRequires:    R-CRAN-qpdf 
Requires:         R-CRAN-openxlsx >= 4.2
Requires:         R-stats >= 4.0
Requires:         R-utils >= 4.0
Requires:         R-CRAN-cli >= 3.4
Requires:         R-CRAN-ggplot2 >= 3.3
Requires:         R-CRAN-reshape2 >= 1.4
Requires:         R-CRAN-kableExtra >= 1.3
Requires:         R-CRAN-minpack.lm >= 1.2
Requires:         R-CRAN-progress >= 1.2
Requires:         R-CRAN-tidyr >= 1.2
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-rlang >= 1.0
Requires:         R-CRAN-purrr >= 0.3
Requires:         R-CRAN-qpdf 

%description
A free software for a fast and easy analysis of 1:1 molecular interaction
studies. This package is suitable for a high-throughput data analysis.
Both the online app and the package are completely open source. You
provide a table of sensogram, tell 'anabel' which method to use, and it
takes care of all fitting details. The first two releases of 'anabel' were
created and implemented as in (<doi:10.1177/1177932218821383>,
<doi:10.1093/database/baz101>).

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
