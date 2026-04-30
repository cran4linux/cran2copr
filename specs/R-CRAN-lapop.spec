%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lapop
%global packver   2.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Processing, Visualizing, and Labeling Americas Barometer Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridtext 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-CRAN-systemfonts 
BuildRequires:    R-CRAN-svglite 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-marginaleffects 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-showtext 
Requires:         R-grid 
Requires:         R-CRAN-gridtext 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sysfonts 
Requires:         R-CRAN-systemfonts 
Requires:         R-CRAN-svglite 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-srvyr 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-haven 
Requires:         R-stats 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-marginaleffects 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-zoo 

%description
Labeling, weighting, and plotting data following custom style guidelines
for use in reports, presentations, and social media posts. The Center for
Global Democracy (formerly the Latin American Public Opinion Project) at
Vanderbilt University is a leader in public survey research, best known
for the Americas Barometer project. The publicly available data can be
downloaded from: <https://www.vanderbilt.edu/lapop/data-access.php>.

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
