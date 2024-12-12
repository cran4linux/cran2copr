%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MAICtools
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Performing Matched-Adjusted Indirect Comparisons (MAIC)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-VIM >= 6.1.0
BuildRequires:    R-graphics >= 4.0.0
BuildRequires:    R-grDevices >= 4.0.0
BuildRequires:    R-grid >= 4.0.0
BuildRequires:    R-stats >= 4.0.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-survival >= 3.2.11
BuildRequires:    R-CRAN-tibble >= 3.1.3
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-boot >= 1.3.28
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-broom >= 0.7.10
BuildRequires:    R-CRAN-survminer >= 0.4.9
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-VIM >= 6.1.0
Requires:         R-graphics >= 4.0.0
Requires:         R-grDevices >= 4.0.0
Requires:         R-grid >= 4.0.0
Requires:         R-stats >= 4.0.0
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-survival >= 3.2.11
Requires:         R-CRAN-tibble >= 3.1.3
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-boot >= 1.3.28
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-broom >= 0.7.10
Requires:         R-CRAN-survminer >= 0.4.9
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-assertthat >= 0.2.1

%description
A generalised workflow for Matching-Adjusted Indirect Comparison (MAIC)
analysis, which supports both anchored and non-anchored MAIC methods.  In
MAIC, unbiased trial outcome comparison is achieved by weighting the
subject-level outcomes of the intervention trial so that the weighted
aggregate measures of prognostic or effect-modifying variables match those
of the comparator trial. Measurements supported include time-to-event
(e.g., overall survival) and binary (e.g., objective tumor response). The
method is described in Signorovitch et al. (2010)
<doi:10.2165/11538370-000000000-00000> and Signorovitch et al. (2012)
<doi:10.1016/j.jval.2012.05.004>.

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
