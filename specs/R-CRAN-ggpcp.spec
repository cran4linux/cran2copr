%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggpcp
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Parallel Coordinate Plots in the 'ggplot2' Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-tibble >= 3.1.4
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-tidyselect >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-tibble >= 3.1.4
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-tidyselect >= 1.1.1
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-assertthat >= 0.2.1

%description
Modern Parallel Coordinate Plots have been introduced in the 1980s as a
way to visualize arbitrarily many numeric variables. This Grammar of
Graphics implementation also incorporates categorical variables into the
plots in a principled manner. By separating the data managing part from
the visual rendering, we give full access to the users while keeping the
number of parameters manageably low.

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
