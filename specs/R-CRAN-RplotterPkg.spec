%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RplotterPkg
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          R Plotting Functions Using 'ggplot2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-glue >= 1.8.0
BuildRequires:    R-CRAN-aplpack >= 1.3.5
BuildRequires:    R-CRAN-data.table >= 1.16.4
BuildRequires:    R-CRAN-rlang >= 1.1.4
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-gtable >= 0.3.6
BuildRequires:    R-CRAN-gt >= 0.11.1
BuildRequires:    R-CRAN-ggplotify >= 0.1.2
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-glue >= 1.8.0
Requires:         R-CRAN-aplpack >= 1.3.5
Requires:         R-CRAN-data.table >= 1.16.4
Requires:         R-CRAN-rlang >= 1.1.4
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-gtable >= 0.3.6
Requires:         R-CRAN-gt >= 0.11.1
Requires:         R-CRAN-ggplotify >= 0.1.2
Requires:         R-methods 

%description
Makes it easy to produce everyday 'ggplot2' charts in a functional way
without an extensive "tree" implementation. The package includes over 15
functions for the production and arrangement of basic graphing.

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
