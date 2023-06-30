%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  doudpackage
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Create Elegant Table 1 in HTML for Bio-Statistics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-kableExtra 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Creates the "table one" of bio-medical papers. Fill it with your data and
the name of the variable which you'll make the group(s) out of and it will
make univariate, bivariate analysis and parse it into HTML. It also allows
you to visualize all your data with graphic representation.

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
