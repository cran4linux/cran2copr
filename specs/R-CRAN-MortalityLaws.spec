%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MortalityLaws
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Mortality Models, Life Tables and HMD

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl >= 1.95
BuildRequires:    R-CRAN-httr >= 1.4.5
BuildRequires:    R-CRAN-pbapply >= 1.3.4
BuildRequires:    R-CRAN-minpack.lm >= 1.2
BuildRequires:    R-CRAN-rvest >= 1.0.3
BuildRequires:    R-CRAN-tidyr >= 0.8.1
BuildRequires:    R-methods 
Requires:         R-CRAN-RCurl >= 1.95
Requires:         R-CRAN-httr >= 1.4.5
Requires:         R-CRAN-pbapply >= 1.3.4
Requires:         R-CRAN-minpack.lm >= 1.2
Requires:         R-CRAN-rvest >= 1.0.3
Requires:         R-CRAN-tidyr >= 0.8.1
Requires:         R-methods 

%description
Fit the most popular human mortality 'laws', and construct full and
abridge life tables given various input indices. A mortality law is a
parametric function that describes the dying-out process of individuals in
a population during a significant portion of their life spans. For a
comprehensive review of the most important mortality laws see Tabeau
(2001) <doi:10.1007/0-306-47562-6_1>. Practical functions for downloading
data from various human mortality databases are provided as well.

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
