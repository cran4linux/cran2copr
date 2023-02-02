%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  suddengains
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Identify Sudden Gains in Longitudinal Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-psych >= 1.8.12
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-patchwork >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-ggrepel >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-naniar 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-psych >= 1.8.12
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-patchwork >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-ggrepel >= 0.8.0
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-naniar 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-cli 

%description
Identify sudden gains based on the three criteria outlined by Tang and
DeRubeis (1999) <doi:10.1037/0022-006X.67.6.894> to a selection of
repeated measures. Sudden losses, defined as the opposite of sudden gains
can also be identified. Two different datasets can be created, one
including all sudden gains/losses and one including one selected sudden
gain/loss for each case. It can extract scores around sudden gains/losses.
It can plot the average change around sudden gains/losses and trajectories
of individual cases.

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
