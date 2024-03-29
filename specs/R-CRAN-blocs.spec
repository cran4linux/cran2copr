%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  blocs
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate and Visualize Voting Blocs' Partisan Contributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-mgcv >= 1.8.39
BuildRequires:    R-CRAN-collapse >= 1.7.6
BuildRequires:    R-CRAN-ks >= 1.13.4
BuildRequires:    R-CRAN-dplyr >= 1.0.6
BuildRequires:    R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-mgcv >= 1.8.39
Requires:         R-CRAN-collapse >= 1.7.6
Requires:         R-CRAN-ks >= 1.13.4
Requires:         R-CRAN-dplyr >= 1.0.6
Requires:         R-CRAN-rlang >= 1.0.0

%description
Functions to combine data on voting blocs' size, turnout, and vote choice
to estimate each bloc's vote contributions to the Democratic and
Republican parties. The package also includes functions for uncertainty
estimation and plotting. Users may define voting blocs along a discrete or
continuous variable. The package implements methods described in Grimmer,
Marble, and Tanigawa-Lau (2023) <doi:10.31235/osf.io/c9fkg>.

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
