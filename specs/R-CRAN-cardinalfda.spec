%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cardinalfda
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          FDA Safety Tables and Figures

License:          Apache License (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-gtsummary >= 2.5.1
BuildRequires:    R-CRAN-dplyr >= 1.2.0
BuildRequires:    R-CRAN-cards >= 0.8.1
BuildRequires:    R-CRAN-cardx >= 0.3.4
BuildRequires:    R-CRAN-crane >= 0.3.1
Requires:         R-CRAN-gtsummary >= 2.5.1
Requires:         R-CRAN-dplyr >= 1.2.0
Requires:         R-CRAN-cards >= 0.8.1
Requires:         R-CRAN-cardx >= 0.3.4
Requires:         R-CRAN-crane >= 0.3.1

%description
Provides implementations of safety tables and figures recommended by the
FDA (U.S. Food and Drug Administration) for clinical trial reporting.
Functions generate standard outputs for adverse events, laboratory
abnormalities, vital signs, exposure, and other safety domains following
the FDA's Safety Reporting guidelines. Outputs are built on the
'gtsummary', 'cards', and 'cardx' frameworks, enabling reproducible and
submission-ready clinical trial safety summaries.

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
