%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gbm.auto
%global packver   2024.10.01
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.10.01
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Boosted Regression Tree Modelling and Mapping Suite

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-stats >= 3.3.1
BuildRequires:    R-CRAN-ggmap >= 3.0.2
BuildRequires:    R-CRAN-readr >= 2.1.4
BuildRequires:    R-CRAN-gbm >= 2.1.1
BuildRequires:    R-CRAN-lubridate >= 1.9.2
BuildRequires:    R-CRAN-stringi >= 1.6.1
BuildRequires:    R-CRAN-mapplots >= 1.5
BuildRequires:    R-CRAN-dismo >= 1.3.14
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-beepr >= 1.2
BuildRequires:    R-CRAN-ggspatial >= 1.1.9
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-sf >= 0.9.7
BuildRequires:    R-CRAN-viridis >= 0.6.4
BuildRequires:    R-CRAN-stars >= 0.6.3
BuildRequires:    R-CRAN-starsExtra >= 0.2.7
BuildRequires:    R-CRAN-Metrics >= 0.1.4
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-stats >= 3.3.1
Requires:         R-CRAN-ggmap >= 3.0.2
Requires:         R-CRAN-readr >= 2.1.4
Requires:         R-CRAN-gbm >= 2.1.1
Requires:         R-CRAN-lubridate >= 1.9.2
Requires:         R-CRAN-stringi >= 1.6.1
Requires:         R-CRAN-mapplots >= 1.5
Requires:         R-CRAN-dismo >= 1.3.14
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-beepr >= 1.2
Requires:         R-CRAN-ggspatial >= 1.1.9
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-sf >= 0.9.7
Requires:         R-CRAN-viridis >= 0.6.4
Requires:         R-CRAN-stars >= 0.6.3
Requires:         R-CRAN-starsExtra >= 0.2.7
Requires:         R-CRAN-Metrics >= 0.1.4
Requires:         R-CRAN-lifecycle 

%description
Automates delta log-normal boosted regression tree abundance prediction.
Loops through parameters provided (LR (learning rate), TC (tree
complexity), BF (bag fraction)), chooses best, simplifies, & generates
line, dot & bar plots, & outputs these & predictions & a report, makes
predicted abundance maps, and Unrepresentativeness surfaces.  Package core
built around 'gbm' (gradient boosting machine) functions in 'dismo'
(Hijmans, Phillips, Leathwick & Jane Elith, 2020 & ongoing), itself built
around 'gbm' (Greenwell, Boehmke, Cunningham & Metcalfe, 2020 & ongoing,
originally by Ridgeway). Indebted to Elith/Leathwick/Hastie 2008 'Working
Guide' <doi:10.1111/j.1365-2656.2008.01390.x>; workflow follows Appendix
S3. See <https://www.simondedman.com/> for published guides and papers
using this package.

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
