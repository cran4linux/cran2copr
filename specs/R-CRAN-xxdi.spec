%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xxdi
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package for Evaluating Scholarly Expertise Indices for Institutional Research Assessment

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.2.0
Requires:         R-core >= 4.4.2.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.3.3
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-Matrix >= 1.6.1.1
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-agop >= 0.2.4
Requires:         R-stats >= 4.3.3
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-Matrix >= 1.6.1.1
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-agop >= 0.2.4

%description
Institutional performance assessment remains a key challenge to a
multitude of stakeholders. Existing indicators such as h-type indicators,
g-type indicators, and many others do not reflect expertise of
institutions that defines their research portfolio. The package offers
functionality to compute and visualise two novel indices: the x-index and
the xd-index. The x-index evaluates an institution's scholarly expertise
within a specific discipline or field, while the xd-index provides a
broader assessment of overall scholarly expertise considering an
institution's publication pattern and strengths across coarse thematic
areas. These indices offer a nuanced understanding of institutional
research capabilities, aiding stakeholders in research management and
resource allocation decisions. Lathabai, H.H., Nandy, A., and Singh, V.K.
(2021) <doi:10.1007/s11192-021-04188-3>. Nandy, A., Lathabai, H.H., and
Singh, V.K. (2023) <doi:10.5281/zenodo.8305585>. This package provides the
h-, g-, x-, xd-indices, and their variants for use with standard format of
Web of Science (WoS) scrapped datasets.

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
