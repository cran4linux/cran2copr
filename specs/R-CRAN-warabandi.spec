%global __brp_check_rpaths %{nil}
%global packname  warabandi
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Roster Generation of Turn for Weekdays:'warabandi'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-readtext 
BuildRequires:    R-CRAN-flextable 
Requires:         R-CRAN-lubridate 
Requires:         R-utils 
Requires:         R-CRAN-readtext 
Requires:         R-CRAN-flextable 

%description
It generates the roster of turn for an outlet which is flowing (water)
24X7 or 168 hours towards the area under command or agricutural area (to
be irrigated). The area under command is differentially owned by different
individual farmers. The Outlet runs for free of cost to irrigate the area
under command 24X7. So, flow time of the outlet has to be divided based on
an area owned by an individual farmer and the location of his land or
farm. This roster is known as 'warabandi' and its generation in
agriculture practices is a very tedious task. Calculations of time in
microseconds are more error-prone, especially whenever it is performed by
hands. That division of flow time for an individual farmer can be
calculated by 'warabandi'. However, it generates a full publishable report
for an outlet and all the farmers who have farms subjected to be
irrigated. It reduces error risk and makes a more reproducible roster. For
more details about warabandi system you can found elsewhere in Bandaragoda
DJ(1995) <https://publications.iwmi.org/pdf/H_17571i.pdf>.

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
