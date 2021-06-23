%global __brp_check_rpaths %{nil}
%global packname  gbm.auto
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Boosted Regression Tree Modelling and Mapping Suite

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.1
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-gbm >= 2.1.1
BuildRequires:    R-CRAN-mapplots >= 1.5
BuildRequires:    R-CRAN-beepr >= 1.2
BuildRequires:    R-CRAN-rgdal >= 1.1.10
BuildRequires:    R-CRAN-dismo >= 1.0.15
BuildRequires:    R-CRAN-sf >= 0.9.7
BuildRequires:    R-CRAN-maptools >= 0.9.1
BuildRequires:    R-CRAN-shapefiles >= 0.7
BuildRequires:    R-CRAN-rgeos >= 0.3.19
Requires:         R-stats >= 3.3.1
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-gbm >= 2.1.1
Requires:         R-CRAN-mapplots >= 1.5
Requires:         R-CRAN-beepr >= 1.2
Requires:         R-CRAN-rgdal >= 1.1.10
Requires:         R-CRAN-dismo >= 1.0.15
Requires:         R-CRAN-sf >= 0.9.7
Requires:         R-CRAN-maptools >= 0.9.1
Requires:         R-CRAN-shapefiles >= 0.7
Requires:         R-CRAN-rgeos >= 0.3.19

%description
Automates delta log-normal boosted regression tree abundance prediction.
Loops through parameters provided (LR (learning rate), TC (tree
complexity), BF (bag fraction)), chooses best, simplifies, & generates
line, dot & bar plots, & outputs these & predictions & a report, makes
predicted abundance maps, and Unrepresentativeness surfaces. Package core
built around 'gbm' (gradient boosting machine) functions in 'dismo'
(Hijmans, Phillips, Leathwick & Jane Elith, 2020 & ongoing), itself built
around 'gbm' (Greenwell, Boehmke, Cunningham & Metcalfe, 2020 & ongoing,
originally by Ridgeway). Indebted to Elith/Leathwick/Hastie 2008 'Working
Guide' <doi:10.1111/j.1365-2656.2008.01390.x>; workflow follows Appendix
S3. See <http://www.simondedman.com/> for published guides and papers
using this package.

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
