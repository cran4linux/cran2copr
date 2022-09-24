%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tetragon
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Sequence Prediction by Expansion of the Distance Matrix

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-imputeTS >= 3.2
BuildRequires:    R-CRAN-modeest >= 2.4.0
BuildRequires:    R-CRAN-Rfast >= 2.0.6
BuildRequires:    R-CRAN-readr >= 2.0.1
BuildRequires:    R-CRAN-lubridate >= 1.7.10
BuildRequires:    R-CRAN-fastDummies >= 1.6.3
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-entropy >= 1.3.1
BuildRequires:    R-CRAN-scales >= 1.1.1
BuildRequires:    R-CRAN-tictoc >= 1.0
BuildRequires:    R-CRAN-greybox >= 1.0.1
BuildRequires:    R-CRAN-fANCOVA >= 0.6.1
BuildRequires:    R-CRAN-philentropy >= 0.5.0
BuildRequires:    R-CRAN-narray >= 0.4.1.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-dqrng >= 0.3.0
BuildRequires:    R-CRAN-moments >= 0.14
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-imputeTS >= 3.2
Requires:         R-CRAN-modeest >= 2.4.0
Requires:         R-CRAN-Rfast >= 2.0.6
Requires:         R-CRAN-readr >= 2.0.1
Requires:         R-CRAN-lubridate >= 1.7.10
Requires:         R-CRAN-fastDummies >= 1.6.3
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-entropy >= 1.3.1
Requires:         R-CRAN-scales >= 1.1.1
Requires:         R-CRAN-tictoc >= 1.0
Requires:         R-CRAN-greybox >= 1.0.1
Requires:         R-CRAN-fANCOVA >= 0.6.1
Requires:         R-CRAN-philentropy >= 0.5.0
Requires:         R-CRAN-narray >= 0.4.1.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-dqrng >= 0.3.0
Requires:         R-CRAN-moments >= 0.14

%description
Each sequence is predicted by expanding the distance matrix. The compact
set of hyper-parameters is tuned through random search.

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
