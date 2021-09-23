%global __brp_check_rpaths %{nil}
%global packname  orderly
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Lightweight Reproducible Reporting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RSQLite >= 2.2.4
BuildRequires:    R-CRAN-zip >= 2.0.0
BuildRequires:    R-CRAN-fs >= 1.2.7
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-docopt 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-ids 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-RSQLite >= 2.2.4
Requires:         R-CRAN-zip >= 2.0.0
Requires:         R-CRAN-fs >= 1.2.7
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-docopt 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-ids 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 

%description
Order, create and store reports from R.  By defining a lightweight
interface around the inputs and outputs of an analysis, a lot of the
repetitive work for reproducible research can be automated.  We define a
simple format for organising and describing work that facilitates
collaborative reproducible research and acknowledges that all analyses are
run multiple times over their lifespans.

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
