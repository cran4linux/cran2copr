%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crane
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Supplements the 'gtsummary' Package for Pharmaceutical Reporting

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.4
BuildRequires:    R-CRAN-gtsummary >= 2.1.0
BuildRequires:    R-CRAN-rlang >= 1.1.5
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-flextable >= 0.9.7
BuildRequires:    R-CRAN-gt >= 0.11.1
Requires:         R-CRAN-cli >= 3.6.4
Requires:         R-CRAN-gtsummary >= 2.1.0
Requires:         R-CRAN-rlang >= 1.1.5
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-flextable >= 0.9.7
Requires:         R-CRAN-gt >= 0.11.1

%description
Tables summarizing clinical trial results are often complex and require
detailed tailoring prior to submission to a health authority.  The 'crane'
package supplements the functionality of the 'gtsummary' package for
creating these often highly bespoke tables in the pharmaceutical industry.

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
