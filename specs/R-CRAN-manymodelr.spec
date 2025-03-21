%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  manymodelr
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Build and Tune Several Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0.88
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-e1071 >= 1.7.8
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-lme4 >= 1.1.27.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-Metrics >= 0.1.4
Requires:         R-CRAN-caret >= 6.0.88
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-e1071 >= 1.7.8
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-lme4 >= 1.1.27.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-Metrics >= 0.1.4

%description
Frequently one needs a convenient way to build and tune several models in
one go.The goal is to provide a number of machine learning convenience
functions. It provides the ability to build, tune and obtain predictions
of several models in one function. The models are built using functions
from 'caret' with easier to read syntax. Kuhn(2014)
<doi:10.48550/arXiv.1405.6974>.

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
