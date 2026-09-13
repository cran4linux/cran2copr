%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  coreval
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Check Clinical Trial Data Against 'CDISC' Open Rules

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-haven 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-haven 

%description
Finds conformance problems in clinical trial data without leaving R, using
the openly published 'CDISC' Open Rules ('CORE'). Check a single dataset
while you are still writing the code that builds it, or a whole study
folder once it exists, and get the findings back as a tidy data frame
pointing at the exact row and variable. Reads transport ('XPT'), 'SAS' and
comma-separated files, plus 'Define-XML' when present, and covers rules
for the 'SDTM', 'SEND' and 'TIG' standards. The rules are bundled inside
the package, so nothing is downloaded and your data never leaves your
machine: no internet, no API key, no account. When a rule cannot be
checked - because it needs a dataset you did not supply, for instance - it
is reported as skipped with the reason, never counted as a pass. Meant as
a quick first pass before a qualified validation system, never as a
replacement for one. An independent project: not affiliated with or
endorsed by 'CDISC', and not a 'CORE'-certified conformance engine.

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
