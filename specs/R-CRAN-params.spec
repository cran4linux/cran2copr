%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  params
%global packver   0.7.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.7
Release:          1%{?dist}%{?buildtag}
Summary:          Simplify Parameters

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppTOML 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-whisker 
Requires:         R-utils 
Requires:         R-CRAN-RcppTOML 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-purrr 

%description
An interface to simplify organizing parameters used in a package, using
external configuration files. This attempts to provide a cleaner
alternative to options().

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
