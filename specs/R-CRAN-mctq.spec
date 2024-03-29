%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mctq
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Process the Munich ChronoType Questionnaire (MCTQ)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.1
BuildRequires:    R-CRAN-checkmate >= 2.1.0
BuildRequires:    R-CRAN-lubridate >= 1.9.2
BuildRequires:    R-CRAN-hms >= 1.1.2
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-lifecycle >= 1.0.3
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.1
Requires:         R-CRAN-checkmate >= 2.1.0
Requires:         R-CRAN-lubridate >= 1.9.2
Requires:         R-CRAN-hms >= 1.1.2
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-lifecycle >= 1.0.3

%description
A complete toolkit to process the Munich ChronoType Questionnaire (MCTQ)
for its three versions (standard, micro, and shift). MCTQ is a
quantitative and validated tool to assess chronotypes using peoples' sleep
behavior, originally presented by Till Roenneberg, Anna Wirz-Justice, and
Martha Merrow (2003, <doi:10.1177/0748730402239679>).

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
