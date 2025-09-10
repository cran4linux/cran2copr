%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  autotesteR
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Functions for Basic Statistical Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-FSA 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-car 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-FSA 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-nortest 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides simple and intuitive functions for basic statistical analyses.
Methods include the t-test (Student 1908 <doi:10.1093/biomet/6.1.1>), the
Mann-Whitney U test (Mann and Whitney 1947 <doi:10.1214/aoms/1177730491>),
Pearson's correlation (Pearson 1895 <doi:10.1098/rspl.1895.0041>), and
analysis of variance (Fisher 1925, <doi:10.1007/978-1-4612-4380-9_5>).
Functions are compatible with 'ggplot2' and 'dplyr'.

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
