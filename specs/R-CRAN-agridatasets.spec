%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agridatasets
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive Collection of Agricultural and Agronomic Datasets

License:          GPL (>= 2) | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
Offers a rich and diverse collection of datasets focused on agriculture,
agronomy, animal science, and related fields. The package includes
experimental, observational, and field-trial data on crops such as rice,
wheat, corn, soybean, cotton, coffee, avocado, and orange, as well as
forestry species including bamboo, eucalyptus, and timber. Datasets cover
plant breeding and genetics, factorial and randomized block experiments,
herbicide and insecticide efficacy trials, pest and disease infestation,
soil characteristics and land suitability, plant growth regulators, seed
germination, and crop yield modeling. Additional datasets address animal
science topics such as cattle insemination and conception, pig and broiler
growth, lamb births, and toxicology studies on aquatic and non-target
species. Data sources include peer-reviewed agronomic studies, uniformity
and Latin square field trials, glasshouse experiments, and international
agricultural surveys. Designed for agronomists, researchers, plant and
animal scientists, data scientists, and students, this package facilitates
exploratory data analysis, statistical modeling, and hypothesis testing in
agricultural and biological sciences. The package includes datasets
originally distributed in other R packages. The original authors and
contributors associated with these source packages and datasets are
acknowledged in Authors@R, and the original sources and applicable
licensing terms are documented in LICENSES_DETAILS.md.

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
