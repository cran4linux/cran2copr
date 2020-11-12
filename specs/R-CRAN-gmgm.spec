%global packname  gmgm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Mixture Graphical Model Learning and Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-visNetwork >= 2.0.8
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-purrr >= 0.3.3
Requires:         R-stats >= 3.5.0
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-visNetwork >= 2.0.8
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-purrr >= 0.3.3

%description
Gaussian mixture graphical models include Bayesian networks and dynamic
Bayesian networks (their temporal extension) whose local probability
distributions are described by Gaussian mixture models. They are powerful
tools for graphically and quantitatively representing nonlinear
dependencies between continuous variables. This package provides a
complete framework to create, manipulate, learn the structure and the
parameters, and perform inference in these models. Most of the algorithms
are described in the PhD thesis of Roos (2018)
<https://tel.archives-ouvertes.fr/tel-01943718>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
