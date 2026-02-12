%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  artma
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Replication Tools for Meta-Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-metafor >= 4.8.0
BuildRequires:    R-CRAN-cli >= 3.6.5
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-lintr >= 3.2.0
BuildRequires:    R-CRAN-sandwich >= 3.1.0
BuildRequires:    R-CRAN-withr >= 3.0.2
BuildRequires:    R-CRAN-plm >= 2.6.3
BuildRequires:    R-CRAN-yaml >= 2.3.10
BuildRequires:    R-CRAN-memoise >= 2.0.1
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-lmtest >= 0.9.40
BuildRequires:    R-CRAN-NlcOptim >= 0.6
BuildRequires:    R-CRAN-climenu >= 0.1.3
BuildRequires:    R-CRAN-ggtext >= 0.1.2
Requires:         R-CRAN-metafor >= 4.8.0
Requires:         R-CRAN-cli >= 3.6.5
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-lintr >= 3.2.0
Requires:         R-CRAN-sandwich >= 3.1.0
Requires:         R-CRAN-withr >= 3.0.2
Requires:         R-CRAN-plm >= 2.6.3
Requires:         R-CRAN-yaml >= 2.3.10
Requires:         R-CRAN-memoise >= 2.0.1
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-lmtest >= 0.9.40
Requires:         R-CRAN-NlcOptim >= 0.6
Requires:         R-CRAN-climenu >= 0.1.3
Requires:         R-CRAN-ggtext >= 0.1.2

%description
Provides a unified and straightforward interface for performing a variety
of meta-analysis methods directly from user data. Users can input a data
frame, specify key parameters, and effortlessly execute and compare
multiple common meta-analytic models. Designed for immediate usability,
the package facilitates transparent, reproducible research without manual
implementation of each analytical method. Ideal for researchers aiming for
efficiency and reproducibility, it streamlines workflows from data
preparation to results interpretation.

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
