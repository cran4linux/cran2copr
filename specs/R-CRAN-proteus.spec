%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  proteus
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multiform Seq2Seq Model for Time-Feature Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-ggthemes >= 4.2.4
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-imputeTS >= 3.1
BuildRequires:    R-CRAN-modeest >= 2.4.0
BuildRequires:    R-CRAN-lubridate >= 1.7.9.2
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-readr >= 1.4.0
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-future >= 1.33.0
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-greybox >= 1.0.7
BuildRequires:    R-CRAN-dplyr >= 1.0.2
BuildRequires:    R-CRAN-tictoc >= 1.0.1
BuildRequires:    R-CRAN-fANCOVA >= 0.6.1
BuildRequires:    R-CRAN-narray >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-furrr >= 0.3.1
BuildRequires:    R-CRAN-torch >= 0.3.0
BuildRequires:    R-CRAN-moments >= 0.14
Requires:         R-CRAN-ggthemes >= 4.2.4
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-imputeTS >= 3.1
Requires:         R-CRAN-modeest >= 2.4.0
Requires:         R-CRAN-lubridate >= 1.7.9.2
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-readr >= 1.4.0
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-future >= 1.33.0
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-greybox >= 1.0.7
Requires:         R-CRAN-dplyr >= 1.0.2
Requires:         R-CRAN-tictoc >= 1.0.1
Requires:         R-CRAN-fANCOVA >= 0.6.1
Requires:         R-CRAN-narray >= 0.4.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-furrr >= 0.3.1
Requires:         R-CRAN-torch >= 0.3.0
Requires:         R-CRAN-moments >= 0.14

%description
Seq2seq time-feature analysis based on variational model, with a wide
range of distributions available for the latent variable.

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
