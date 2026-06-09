%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  msmtools
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Building Augmented Data to Run Multi-State Models with 'msm' Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.3
BuildRequires:    R-CRAN-survival >= 3.8.6
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-msm >= 1.8.2
BuildRequires:    R-CRAN-data.table >= 1.18.4
Requires:         R-CRAN-ggplot2 >= 4.0.3
Requires:         R-CRAN-survival >= 3.8.6
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-msm >= 1.8.2
Requires:         R-CRAN-data.table >= 1.18.4

%description
A fast and general method for restructuring classical longitudinal
observational data into augmented transition data suitable for multi-state
modeling with the 'msm' package. Works with any longitudinal data where
subjects accumulate repeated observations with start and end times and an
optional terminal outcome. Methods are described in Grossetti, Ieva and
Paganoni (2018) <doi:10.1007/s10729-017-9400-z>.

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
