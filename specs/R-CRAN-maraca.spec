%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  maraca
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          The Maraca Plot: Visualization of Hierarchical Composite Endpoints in Clinical Trials

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3
BuildRequires:    R-CRAN-survival >= 3.3
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-checkmate >= 2.1
BuildRequires:    R-CRAN-tidyr >= 1.2
BuildRequires:    R-CRAN-dplyr >= 1.0
BuildRequires:    R-CRAN-ggfortify >= 0.4
BuildRequires:    R-CRAN-hce >= 0.0.2
Requires:         R-CRAN-ggplot2 >= 3.3
Requires:         R-CRAN-survival >= 3.3
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-checkmate >= 2.1
Requires:         R-CRAN-tidyr >= 1.2
Requires:         R-CRAN-dplyr >= 1.0
Requires:         R-CRAN-ggfortify >= 0.4
Requires:         R-CRAN-hce >= 0.0.2

%description
Library that supports visual interpretation of hierarchical composite
endpoints (HCEs). HCEs are complex constructs used as primary endpoints in
clinical trials, combining outcomes of different types into ordinal
endpoints, in which each patient contributes the most clinically important
event (one and only one) to the analysis.

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
