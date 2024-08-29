%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FishProxCompAnalyzer
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Proximate Composition Analysis of Fish and Feed Ingredients

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The proximate composition analysis is the quantification of main
components that constitutes nutritional profile of any food and food
products including fish, shellfish, fish feed and their ingredients.
Understanding this composition is essential for evaluating their
nutritional value and for making informed dietary choices. The primary
components typically analyzed include; moisture/ water in foods, crude
protein, crude fat/ lipid, total ash, fiber and carbohydrates
AOAC(2005,ISBN:0-935584-77-3). In case of fish, shellfish and its
products, the proximate composition consists of four primary constituents
- water, protein, fat, and ash (mostly minerals). Fish exhibit significant
variation in their chemical makeup based on age, sex, environment, and
season, both within the same species and between individual fish. There is
minimal fluctuation in the content of ash and protein. The lipid
concentration varies remarkably and is inversely correlated with the water
content. In case of fish, carbohydrates are present in minor quantity so
that are quantified by subtracting total of other components from 100 to
get percentage of carbohydrates.

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
