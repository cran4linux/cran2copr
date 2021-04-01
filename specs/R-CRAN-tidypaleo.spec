%global packname  tidypaleo
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Tools for Paleoenvironmental Archives

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.2
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-styler 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggstance 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rioja 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tidyr >= 1.0.2
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-styler 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggstance 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rioja 

%description
Provides a set of functions with a common framework for age-depth model
management, stratigraphic visualization, and common statistical
transformations. The focus of the package is stratigraphic visualization,
for which 'ggplot2' components are provided to reproduce the scales,
geometries, facets, and theme elements commonly used in
publication-quality stratigraphic diagrams. Helpers are also provided to
reproduce the exploratory statistical summaries that are frequently
included on stratigraphic diagrams.

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
