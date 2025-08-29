%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fanyi
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Translate Words or Sentences via Online Translators

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-yulab.utils >= 0.1.6
BuildRequires:    R-CRAN-ggfun >= 0.1.3
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rentrez 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-SSEparser 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-yulab.utils >= 0.1.6
Requires:         R-CRAN-ggfun >= 0.1.3
Requires:         R-CRAN-digest 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rentrez 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-SSEparser 
Requires:         R-utils 
Requires:         R-CRAN-uuid 

%description
Useful functions to translate text for multiple languages using online
translators. For example, by translating error messages and descriptive
analysis results into a language familiar to the user, it enables a better
understanding of the information, thereby reducing the barriers caused by
language. It offers several helper functions to query gene information to
help interpretation of interested genes (e.g., marker genes, differential
expression genes), and provides utilities to translate 'ggplot' graphics.
This package is not affiliated with any of the online translators. The
developers do not take responsibility for the invoice it incurs when using
this package, especially for exceeding the free quota.

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
