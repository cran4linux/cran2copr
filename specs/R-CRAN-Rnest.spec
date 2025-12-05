%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rnest
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Next Eigenvalue Sufficiency Test

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.58.1
BuildRequires:    R-CRAN-cli >= 3.6.4
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-crayon >= 1.4.0
BuildRequires:    R-CRAN-EFA.MRFA >= 1.1.2
BuildRequires:    R-CRAN-mvtnorm >= 1.1
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-lavaan >= 0.6
Requires:         R-CRAN-MASS >= 7.3.58.1
Requires:         R-CRAN-cli >= 3.6.4
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-crayon >= 1.4.0
Requires:         R-CRAN-EFA.MRFA >= 1.1.2
Requires:         R-CRAN-mvtnorm >= 1.1
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-lavaan >= 0.6

%description
Determine the number of dimensions to retain in exploratory factor
analysis. The main function, nest(), returns the solution and the
plot(nest()) returns a plot.

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
