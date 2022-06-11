%global __brp_check_rpaths %{nil}
%global packname  hardhat
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Construct Modeling Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.1.7
BuildRequires:    R-CRAN-glue >= 1.6.2
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-vctrs >= 0.4.1
Requires:         R-CRAN-tibble >= 3.1.7
Requires:         R-CRAN-glue >= 1.6.2
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-vctrs >= 0.4.1

%description
Building modeling packages is hard. A large amount of effort generally
goes into providing an implementation for a new method that is efficient,
fast, and correct, but often less emphasis is put on the user interface. A
good interface requires specialized knowledge about S3 methods and
formulas, which the average package developer might not have.  The goal of
'hardhat' is to reduce the burden around building new modeling packages by
providing functionality for preprocessing, predicting, and validating
input.

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
