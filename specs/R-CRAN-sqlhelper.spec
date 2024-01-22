%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sqlhelper
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easier 'SQL' Integration

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pool 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pool 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rlang 

%description
Execute files of 'SQL' and manage database connections. 'SQL' statements
and queries may be interpolated with string literals. Execution of
individual statements and queries may be controlled with keywords.
Multiple connections may be defined with 'YAML' and accessed by name.

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
