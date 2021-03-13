%global packname  jtools
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Presentation of Social Scientific Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-pkgconfig 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-pkgconfig 
Requires:         R-CRAN-tibble 

%description
This is a collection of tools that the author (Jacob) has written for the
purpose of more efficiently understanding and sharing the results of
(primarily) regression analyses. There are also a number of miscellaneous
functions for statistical and programming purposes. Just about everything
supports models from the survey package.

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
