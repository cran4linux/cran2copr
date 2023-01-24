%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rdracor
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Access to the 'DraCor' API

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.8
BuildRequires:    R-CRAN-Rdpack >= 2.4
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.1
BuildRequires:    R-CRAN-igraph >= 1.2.4.1
BuildRequires:    R-CRAN-xml2 >= 1.2.2
BuildRequires:    R-CRAN-tidyr >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.12.2
BuildRequires:    R-CRAN-purrr >= 0.3.5
BuildRequires:    R-utils 
Requires:         R-CRAN-tibble >= 3.1.8
Requires:         R-CRAN-Rdpack >= 2.4
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.1
Requires:         R-CRAN-igraph >= 1.2.4.1
Requires:         R-CRAN-xml2 >= 1.2.2
Requires:         R-CRAN-tidyr >= 1.2.1
Requires:         R-CRAN-data.table >= 1.12.2
Requires:         R-CRAN-purrr >= 0.3.5
Requires:         R-utils 

%description
Provide an interface for 'Drama Corpora Project' ('DraCor') API:
<https://dracor.org/documentation/api>.

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
