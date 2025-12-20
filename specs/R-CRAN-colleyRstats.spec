%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  colleyRstats
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Streamline Statistical Analysis and Reporting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-effectsize >= 1.0.1
BuildRequires:    R-CRAN-ggpmisc >= 0.6.3
BuildRequires:    R-CRAN-report >= 0.6.1
BuildRequires:    R-CRAN-ggstatsplot >= 0.13.4
BuildRequires:    R-CRAN-ARTool 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-conflicted 
BuildRequires:    R-CRAN-FSA 
BuildRequires:    R-CRAN-ggsignif 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rstatix 
BuildRequires:    R-CRAN-see 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 >= 4.0.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-effectsize >= 1.0.1
Requires:         R-CRAN-ggpmisc >= 0.6.3
Requires:         R-CRAN-report >= 0.6.1
Requires:         R-CRAN-ggstatsplot >= 0.13.4
Requires:         R-CRAN-ARTool 
Requires:         R-CRAN-car 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-conflicted 
Requires:         R-CRAN-FSA 
Requires:         R-CRAN-ggsignif 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rstatix 
Requires:         R-CRAN-see 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-xtable 

%description
Built upon popular R packages such as 'ggstatsplot' and 'ARTool', this
collection offers a wide array of tools for simplifying reproducible
analyses, generating high-quality visualizations, and producing
'APA'-compliant outputs. The primary goal of this package is to
significantly reduce repetitive coding efforts, allowing you to focus on
interpreting results. Whether you're dealing with ANOVA assumptions,
reporting effect sizes, or creating publication-ready visualizations, this
package makes these tasks easier.

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
