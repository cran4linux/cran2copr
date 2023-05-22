%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kidsides
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download, Cache, and Connect to KidSIDES

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-R.utils 
Requires:         R-tools 

%description
Caches and then connects to a 'sqlite' database containing half a million
pediatric drug safety signals. The database is part of a family of
resources catalogued at <https://nsides.io>. The database contains 17
tables where the description table provides a map between the fields the
field's details. The database was created by Nicholas Giangreco during his
PhD thesis which you can read in Giangreco (2022)
<doi:10.7916/d8-5d9b-6738>. The observations are from the Food and Drug
Administration's Adverse Event Reporting System. Generalized additive
models estimated drug effects across child development stages for the
occurrence of an adverse event when exposed to a drug compared to other
drugs. Read more at the methods detailed in Giangreco (2022)
<doi:10.1016/j.medj.2022.06.001>.

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
