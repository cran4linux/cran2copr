%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StemAnalysis
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reconstructing Tree Growth and Carbon Accumulation with Stem Analysis Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lmfor >= 1.0
Requires:         R-CRAN-lmfor >= 1.0

%description
Use stem analysis data to reconstructing tree growth and carbon
accumulation. Users can independently or in combination perform a number
of standard tasks for any tree species. (i) Age class determination. (ii)
The cumulative growth, mean annual increment, and current annual increment
of diameter at breast height (DBH) with bark, tree height, and stem volume
with bark are estimated. (iii) Tree biomass and carbon storage estimation
from volume and allometric models are calculated. (iv) Height-diameter
relationship is fitted with nonlinear models, if diameter at breast height
(DBH) or tree height are available, which can be used to retrieve tree
height and diameter at breast height (DBH).
<https://github.com/forestscientist/StemAnalysis>.

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
