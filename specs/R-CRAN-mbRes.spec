%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mbRes
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Exploration of Multiple Biomarker Responses using Effect Size

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-tidyr >= 1.2.1
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.14.6
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-forcats >= 0.5.2
BuildRequires:    R-CRAN-purrr >= 0.3.5
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-tidyr >= 1.2.1
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-data.table >= 1.14.6
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-forcats >= 0.5.2
Requires:         R-CRAN-purrr >= 0.3.5
Requires:         R-stats 

%description
Summarize multiple biomarker responses of aquatic organisms to
contaminants using Cliff’s delta, as described in Pham & Sokolova (2022)
<doi:10.1002/ieam.4676>.

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
