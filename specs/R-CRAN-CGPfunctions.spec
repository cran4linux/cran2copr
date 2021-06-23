%global __brp_check_rpaths %{nil}
%global packname  CGPfunctions
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Powell Miscellaneous Functions for Teaching and Learning Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-scales >= 1.1.0
BuildRequires:    R-CRAN-DescTools >= 0.99.32
BuildRequires:    R-CRAN-sjstats >= 0.17.9
BuildRequires:    R-CRAN-BayesFactor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggmosaic 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-paletteer 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-scales >= 1.1.0
Requires:         R-CRAN-DescTools >= 0.99.32
Requires:         R-CRAN-sjstats >= 0.17.9
Requires:         R-CRAN-BayesFactor 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggmosaic 
Requires:         R-CRAN-ggrepel 
Requires:         R-methods 
Requires:         R-CRAN-paletteer 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 

%description
Miscellaneous functions useful for teaching statistics as well as actually
practicing the art. They typically are not new methods but rather wrappers
around either base R or other packages.

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
