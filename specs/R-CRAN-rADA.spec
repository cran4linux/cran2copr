%global __brp_check_rpaths %{nil}
%global packname  rADA
%global packver   1.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis and Cut-Point Determination of Immunoassays

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc >= 4.3.0
BuildRequires:    R-CRAN-openxlsx >= 4.2.2
BuildRequires:    R-grid >= 3.5.3
BuildRequires:    R-stats >= 3.5.3
BuildRequires:    R-grDevices >= 3.5.3
BuildRequires:    R-utils >= 3.5.3
BuildRequires:    R-methods >= 3.5.3
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-lmerTest >= 3.1.0
BuildRequires:    R-CRAN-car >= 3.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-e1071 >= 1.7.2
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-knitr >= 1.29
BuildRequires:    R-CRAN-forestplot >= 1.10
BuildRequires:    R-CRAN-lme4 >= 1.1.21
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-matrixStats >= 0.56.0
Requires:         R-CRAN-Hmisc >= 4.3.0
Requires:         R-CRAN-openxlsx >= 4.2.2
Requires:         R-grid >= 3.5.3
Requires:         R-stats >= 3.5.3
Requires:         R-grDevices >= 3.5.3
Requires:         R-utils >= 3.5.3
Requires:         R-methods >= 3.5.3
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-lmerTest >= 3.1.0
Requires:         R-CRAN-car >= 3.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-e1071 >= 1.7.2
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-knitr >= 1.29
Requires:         R-CRAN-forestplot >= 1.10
Requires:         R-CRAN-lme4 >= 1.1.21
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-matrixStats >= 0.56.0

%description
Systematically transform immunoassay data, evaluate if the data is
normally distributed, and pick the right method for cut point
determination based on that evaluation. This package can also produce
plots that are needed for reports, so data analysis and visualization can
be done easily.

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
