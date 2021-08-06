%global __brp_check_rpaths %{nil}
%global packname  gitlabr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access to the 'Gitlab' API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-tibble >= 1.1
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-shiny >= 0.13.0
BuildRequires:    R-CRAN-arpr 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-tibble >= 1.1
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-shiny >= 0.13.0
Requires:         R-CRAN-arpr 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Provides R functions to access the API of the project and repository
management web application 'GitLab'. For many common tasks (repository
file access, issue assignment and status, commenting) convenience wrappers
are provided, and in addition the full API can be used by specifying
request locations. 'GitLab' is open-source software and can be self-hosted
or used on <https://about.gitlab.com>.

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
