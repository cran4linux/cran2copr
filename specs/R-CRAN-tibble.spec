%global __brp_check_rpaths %{nil}
%global packname  tibble
%global packver   3.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Data Frames

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-pillar >= 1.6.0
BuildRequires:    R-CRAN-rlang >= 0.4.3
BuildRequires:    R-CRAN-fansi >= 0.4.0
BuildRequires:    R-CRAN-vctrs >= 0.3.8
BuildRequires:    R-CRAN-ellipsis >= 0.3.2
BuildRequires:    R-CRAN-lifecycle >= 0.2.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pkgconfig 
BuildRequires:    R-utils 
Requires:         R-CRAN-pillar >= 1.6.0
Requires:         R-CRAN-rlang >= 0.4.3
Requires:         R-CRAN-fansi >= 0.4.0
Requires:         R-CRAN-vctrs >= 0.3.8
Requires:         R-CRAN-ellipsis >= 0.3.2
Requires:         R-CRAN-lifecycle >= 0.2.0
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-pkgconfig 
Requires:         R-utils 

%description
Provides a 'tbl_df' class (the 'tibble') that provides stricter checking
and better formatting than the traditional data frame.

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
