%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rosv
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Client to Access and Operate on the 'Open Source Vulnerability' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-memoise >= 2.0.0
BuildRequires:    R-CRAN-R6 >= 2.0.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.16
BuildRequires:    R-CRAN-digest >= 0.6.0
BuildRequires:    R-CRAN-furrr >= 0.3.0
BuildRequires:    R-utils 
Requires:         R-CRAN-memoise >= 2.0.0
Requires:         R-CRAN-R6 >= 2.0.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.16
Requires:         R-CRAN-digest >= 0.6.0
Requires:         R-CRAN-furrr >= 0.3.0
Requires:         R-utils 

%description
Connect, query, and operate on information available from the 'Open Source
Vulnerability' database <https://osv.dev/>. Although 'CRAN' has
vulnerabilities listed, these are few compared to projects such as 'PyPI'.
With tighter integration between 'R' and 'Python', having an 'R' specific
package to access details about vulnerabilities from various sources is a
worthwhile enterprise.

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
