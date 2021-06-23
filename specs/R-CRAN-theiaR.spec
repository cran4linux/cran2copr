%global __brp_check_rpaths %{nil}
%global packname  theiaR
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Download and Manage Data from Theia

License:          GPL (>= 3.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-XML >= 3.86
BuildRequires:    R-tools >= 3.5
BuildRequires:    R-CRAN-raster >= 2.6
BuildRequires:    R-CRAN-R6 >= 2.3
BuildRequires:    R-CRAN-httr >= 1.3
BuildRequires:    R-CRAN-askpass >= 1.1
Requires:         R-CRAN-XML >= 3.86
Requires:         R-tools >= 3.5
Requires:         R-CRAN-raster >= 2.6
Requires:         R-CRAN-R6 >= 2.3
Requires:         R-CRAN-httr >= 1.3
Requires:         R-CRAN-askpass >= 1.1

%description
Provides a simple interface to search available data provided by Theia
(<https://theia.cnes.fr>), download it, and manage it. Data can be
downloaded based on a search result or from a cart file downloaded from
Theia website.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
