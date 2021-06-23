%global __brp_check_rpaths %{nil}
%global packname  rearrr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rearranging Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Arrange data by a set of methods. Use rearrangers to reorder data points
and mutators to change their values. From basic utilities, to centering
the greatest value, to swirling in 3-dimensional space, 'rearrr' enables
creativity when plotting and experimenting with data.

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
