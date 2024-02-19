%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ppsr
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Power Score

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart >= 4.1.15
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-withr >= 2.4.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-parsnip >= 0.1.5
Requires:         R-CRAN-rpart >= 4.1.15
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-withr >= 2.4.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-parsnip >= 0.1.5

%description
The Predictive Power Score (PPS) is an asymmetric, data-type-agnostic
score that can detect linear or non-linear relationships between two
variables. The score ranges from 0 (no predictive power) to 1 (perfect
predictive power). PPS can be useful for data exploration purposes, in the
same way correlation analysis is. For more information on PPS, see
<https://github.com/paulvanderlaken/ppsr>.

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
