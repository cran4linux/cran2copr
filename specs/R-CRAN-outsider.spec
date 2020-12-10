%global packname  outsider
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Install and Run Programs, Outside of R, Inside of R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-remotes >= 2.0
BuildRequires:    R-CRAN-outsider.base 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-remotes >= 2.0
Requires:         R-CRAN-outsider.base 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-yaml 

%description
Install and run external command-line programs in R through use of
'Docker' <https://www.docker.com/> and online repositories.

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
