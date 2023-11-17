%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  textrecipes
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          Extra 'Recipes' for Text Processing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-recipes >= 1.0.7
BuildRequires:    R-CRAN-generics >= 0.1.0
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-recipes >= 1.0.7
Requires:         R-CRAN-generics >= 0.1.0
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-glue 

%description
Converting text to numerical features requires specifically created
procedures, which are implemented as steps according to the 'recipes'
package. These steps allows for tokenization, filtering, counting (tf and
tfidf) and feature hashing.

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
