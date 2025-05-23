%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gitgadget
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          1%{?dist}%{?buildtag}
Summary:          'Rstudio' Addin for Version Control and Assignment Management using Git

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 3.2
BuildRequires:    R-CRAN-callr >= 2.0.4
BuildRequires:    R-CRAN-shiny >= 1.7.1
BuildRequires:    R-CRAN-usethis >= 1.5.1
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-dplyr >= 0.8.3
BuildRequires:    R-CRAN-shinyFiles >= 0.7.5
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-miniUI >= 0.1.1.1
BuildRequires:    R-CRAN-markdown 
Requires:         R-CRAN-curl >= 3.2
Requires:         R-CRAN-callr >= 2.0.4
Requires:         R-CRAN-shiny >= 1.7.1
Requires:         R-CRAN-usethis >= 1.5.1
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-dplyr >= 0.8.3
Requires:         R-CRAN-shinyFiles >= 0.7.5
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-miniUI >= 0.1.1.1
Requires:         R-CRAN-markdown 

%description
An 'Rstudio' addin for version control that allows users to clone
repositories, create and delete branches, and sync forks on GitHub,
GitLab, etc. Furthermore, the addin uses the GitLab API to allow
instructors to create forks and merge requests for all students/teams with
one click of a button.

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
