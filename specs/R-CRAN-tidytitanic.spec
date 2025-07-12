%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidytitanic
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Dataframes Based on Titanic Passengers and Crew

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
A version of the Titanic survival data tailored for people analytics
demonstrations and practice. While another package, 'titanic', reproduces
the Kaggle competition files with minimal preprocessing, 'tidytitanic'
combines the train and test datasets into the single dataset,
'passengers', for exploration and summary across all passengers. It also
extracts personal identifiers—such as first names, last names, and titles
from the raw 'name' field, enabling demographic analysis. The 'passengers'
data does not cover the crew, but this package also provides the more
bare-bones, crew-containing datasets 'tidy_titanic' and 'flat_titanic'
based on the 'Titanic' data set from 'datasets' for further exploration.
This human-centered data package is designed to support exploratory data
analysis, feature engineering, and pedagogical use cases.

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
