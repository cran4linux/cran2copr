%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tidyclust
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Common API to Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.0
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-Rfast >= 2.0.6
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-flexclust >= 1.3.6
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-dials >= 1.1.0
BuildRequires:    R-CRAN-prettyunits >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.9
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-parsnip >= 1.0.2
BuildRequires:    R-CRAN-hardhat >= 1.0.0
BuildRequires:    R-CRAN-rsample >= 1.0.0
BuildRequires:    R-CRAN-tune >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-CRAN-generics >= 0.1.2
BuildRequires:    R-CRAN-modelenv >= 0.1.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.1.0
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-Rfast >= 2.0.6
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-flexclust >= 1.3.6
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-dials >= 1.1.0
Requires:         R-CRAN-prettyunits >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.9
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-parsnip >= 1.0.2
Requires:         R-CRAN-hardhat >= 1.0.0
Requires:         R-CRAN-rsample >= 1.0.0
Requires:         R-CRAN-tune >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-CRAN-generics >= 0.1.2
Requires:         R-CRAN-modelenv >= 0.1.0
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-utils 

%description
A common interface to specifying clustering models, in the same style as
'parsnip'. Creates unified interface across different functions and
computational engines.

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
