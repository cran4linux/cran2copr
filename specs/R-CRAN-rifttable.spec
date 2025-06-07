%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rifttable
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Results Tables to Bridge the Rift Between Epidemiologists and Their Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-broom >= 0.7.0
BuildRequires:    R-CRAN-risks >= 0.4.3
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-broom >= 0.7.0
Requires:         R-CRAN-risks >= 0.4.3
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-purrr 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Presentation-ready results tables for epidemiologists in an automated,
reproducible fashion. The user provides the final analytical dataset and
specifies the design of the table, with rows and/or columns defined by
exposure(s), effect modifier(s), and estimands as desired, allowing to
show descriptors and inferential estimates in one table -- bridging the
rift between epidemiologists and their data, one table at a time. See
Rothman (2017) <doi:10.1007/s10654-017-0314-3>.

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
