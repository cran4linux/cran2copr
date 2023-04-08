%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dcmodify
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          1%{?dist}%{?buildtag}
Summary:          Modify Data Using Externally Defined Modification Rules

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lumberjack >= 1.3.1
BuildRequires:    R-CRAN-validate >= 1.1.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-settings 
BuildRequires:    R-utils 
Requires:         R-CRAN-lumberjack >= 1.3.1
Requires:         R-CRAN-validate >= 1.1.3
Requires:         R-methods 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-settings 
Requires:         R-utils 

%description
Data cleaning scripts typically contain a lot of 'if this change that'
type of statements. Such statements are typically condensed expert
knowledge. With this package, such 'data modifying rules' are taken out of
the code and become in stead parameters to the work flow. This allows one
to maintain, document, and reason about data modification rules as
separate entities.

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
