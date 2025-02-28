%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  workflows
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.3.0
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-hardhat >= 1.4.1
BuildRequires:    R-CRAN-parsnip >= 1.3.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-recipes >= 1.1.1
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
BuildRequires:    R-CRAN-vctrs >= 0.4.1
BuildRequires:    R-CRAN-sparsevctrs >= 0.2.0
BuildRequires:    R-CRAN-generics >= 0.1.2
BuildRequires:    R-CRAN-modelenv >= 0.1.0
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-cli >= 3.3.0
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-hardhat >= 1.4.1
Requires:         R-CRAN-parsnip >= 1.3.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-recipes >= 1.1.1
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-vctrs >= 0.4.1
Requires:         R-CRAN-sparsevctrs >= 0.2.0
Requires:         R-CRAN-generics >= 0.1.2
Requires:         R-CRAN-modelenv >= 0.1.0
Requires:         R-CRAN-withr 

%description
Managing both a 'parsnip' model and its data preparation steps, such as a
model formula or recipe from 'recipes', can often be challenging. The goal
of 'workflows' is to streamline this process by bundling the model with
its data preparation, all within the same object.

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
