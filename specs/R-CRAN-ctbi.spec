%global __brp_check_rpaths %{nil}
%global packname  ctbi
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Procedure to Clean, Decompose and Aggregate Timeseries

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.1.0
BuildRequires:    R-utils >= 4.1.0
BuildRequires:    R-CRAN-data.table >= 1.14.2
Requires:         R-stats >= 4.1.0
Requires:         R-utils >= 4.1.0
Requires:         R-CRAN-data.table >= 1.14.2

%description
Clean, decompose and aggregate univariate time series following the
procedure "Cyclic/trend decomposition using bin interpolation" and the
Logbox method for flagging outliers, both detailed in Ritter, F.:
Technical note: A procedure to clean, decompose and aggregate time series,
Hydrol. Earth Syst. Sci. Discuss. [preprint], <doi:10.5194/hess-2021-609>,
in review.

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
