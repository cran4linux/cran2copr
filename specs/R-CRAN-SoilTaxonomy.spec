%global __brp_check_rpaths %{nil}
%global packname  SoilTaxonomy
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          A System of Soil Classification for Making and Interpreting Soil Surveys

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-stringr 

%description
Taxonomic dictionaries, formative element lists, and functions related to
the maintenance, development and application of U.S. Soil Taxonomy. Data
and functionality are based on official U.S. Department of Agriculture
sources including the latest edition of the Keys to Soil Taxonomy.
Descriptions and metadata are obtained from the National Soil Information
System or Soil Survey Geographic databases. Other sources are referenced
in the data documentation. Provides tools for understanding and
interacting with concepts in the U.S. Soil Taxonomic System. Most of the
current utilities are for working with taxonomic concepts at the "higher"
taxonomic levels: Order, Suborder, Great Group, and Subgroup.

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
