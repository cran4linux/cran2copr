%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tern
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}%{?buildtag}
Summary:          Create Common TLGs Used in Clinical Trials

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.60
BuildRequires:    R-CRAN-survival >= 3.6.4
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-car >= 3.0.13
BuildRequires:    R-CRAN-Rdpack >= 2.4
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-tibble >= 2.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-scales >= 1.2.0
BuildRequires:    R-CRAN-emmeans >= 1.10.4
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-forcats >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-rtables >= 0.6.11
BuildRequires:    R-CRAN-broom >= 0.5.4
BuildRequires:    R-CRAN-formatters >= 0.5.10
BuildRequires:    R-CRAN-gtable >= 0.3.0
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-nestcolor >= 0.1.1
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-MASS >= 7.3.60
Requires:         R-CRAN-survival >= 3.6.4
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-car >= 3.0.13
Requires:         R-CRAN-Rdpack >= 2.4
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-tibble >= 2.0.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-scales >= 1.2.0
Requires:         R-CRAN-emmeans >= 1.10.4
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-forcats >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-rtables >= 0.6.11
Requires:         R-CRAN-broom >= 0.5.4
Requires:         R-CRAN-formatters >= 0.5.10
Requires:         R-CRAN-gtable >= 0.3.0
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-nestcolor >= 0.1.1
Requires:         R-grid 
Requires:         R-CRAN-labeling 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Table, Listings, and Graphs (TLG) library for common outputs used in
clinical trials.

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
