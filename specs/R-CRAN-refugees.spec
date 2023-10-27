%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  refugees
%global packver   2023.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2023.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          UNHCR Refugee Population Statistics Database

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.2.0
Requires:         R-CRAN-tibble >= 3.2.0

%description
The Refugee Population Statistics Database published by The Office of The
United Nations High Commissioner for Refugees (UNHCR) contains information
about forcibly displaced populations spanning more than 70 years of
statistical activities. It covers displaced populations such as refugees,
asylum-seekers and internally displaced people, including their
demographics. Stateless people are also included, most of who have never
been displaced. The database also reflects the different types of
solutions for displaced populations such as repatriation or resettlement.
More information on the data and methodology can be found on the UNHCR
Refugee Data Finder <https://www.unhcr.org/refugee-statistics/>.

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
