%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coursekata
%global packver   0.14.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.0
Release:          1%{?dist}%{?buildtag}
Summary:          Packages and Functions for 'CourseKata' Courses

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-cli >= 3.2.0
BuildRequires:    R-CRAN-supernova >= 2.5.1
BuildRequires:    R-CRAN-mosaic >= 1.8.3
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-Lock5withR >= 1.2.2
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-dslabs >= 0.7.4
BuildRequires:    R-CRAN-lsr >= 0.5.2
BuildRequires:    R-CRAN-vctrs >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-ggformula >= 0.10.1
BuildRequires:    R-CRAN-yesno >= 0.1.2
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-pak 
BuildRequires:    R-CRAN-palmerpenguins 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-cli >= 3.2.0
Requires:         R-CRAN-supernova >= 2.5.1
Requires:         R-CRAN-mosaic >= 1.8.3
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-Lock5withR >= 1.2.2
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-dslabs >= 0.7.4
Requires:         R-CRAN-lsr >= 0.5.2
Requires:         R-CRAN-vctrs >= 0.4.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ggformula >= 0.10.1
Requires:         R-CRAN-yesno >= 0.1.2
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-pak 
Requires:         R-CRAN-palmerpenguins 
Requires:         R-CRAN-viridisLite 

%description
Easily install and load all packages and functions used in 'CourseKata'
courses. Aid teaching with helper functions and augment generic functions
to provide cohesion between the network of packages. Learn more about
'CourseKata' at <https://coursekata.org>.

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
