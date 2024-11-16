%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  necountries
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Countries of the World

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringi 

%description
Based on Natural Earth <https://www.naturalearthdata.com/>, a subset of
countries can easily be selected with their administrative boundaries,
joined with an external data frame and plotted as a thematic map.

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
