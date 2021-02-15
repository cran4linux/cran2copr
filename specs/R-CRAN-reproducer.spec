%global packname  reproducer
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reproduce Statistical Analyses and Meta-Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.45
BuildRequires:    R-stats >= 3.5.2
BuildRequires:    R-CRAN-openxlsx >= 2.4.0
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-ggplot2 >= 2.0.0
BuildRequires:    R-CRAN-metafor >= 1.9.2
BuildRequires:    R-CRAN-xtable >= 1.7.4
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-httr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-lme4 >= 1.1.10
BuildRequires:    R-CRAN-gridExtra >= 0.9
BuildRequires:    R-CRAN-reshape >= 0.8.8
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-GetoptLong >= 0.1.7
Requires:         R-CRAN-MASS >= 7.3.45
Requires:         R-stats >= 3.5.2
Requires:         R-CRAN-openxlsx >= 2.4.0
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-ggplot2 >= 2.0.0
Requires:         R-CRAN-metafor >= 1.9.2
Requires:         R-CRAN-xtable >= 1.7.4
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-httr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-lme4 >= 1.1.10
Requires:         R-CRAN-gridExtra >= 0.9
Requires:         R-CRAN-reshape >= 0.8.8
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-GetoptLong >= 0.1.7

%description
Includes data analysis functions (e.g., to calculate effect sizes and 95%%
Confidence Intervals (CI) on Standardised Effect Sizes (d) for AB/BA
cross-over repeated-measures experimental designs), data presentation
functions (e.g., density curve overlaid on histogram), and the data sets
analyzed in different research papers in software engineering (e.g.,
related to software defect prediction or multi-site experiment concerning
the extent to which structured abstracts were clearer and more complete
than conventional abstracts) to streamline reproducible research in
software engineering.

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
