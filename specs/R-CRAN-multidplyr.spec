%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multidplyr
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Multi-Process 'dplyr' Backend

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 3.5.1
BuildRequires:    R-CRAN-rlang >= 1.0.6
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.3.6
BuildRequires:    R-CRAN-qs >= 0.24.1
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-callr >= 3.5.1
Requires:         R-CRAN-rlang >= 1.0.6
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.3.6
Requires:         R-CRAN-qs >= 0.24.1
Requires:         R-CRAN-cli 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
Partition a data frame across multiple worker processes to provide simple
multicore parallelism.

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
