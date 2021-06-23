%global __brp_check_rpaths %{nil}
%global packname  pander
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}%{?buildtag}
Summary:          An R 'Pandoc' Writer

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-digest 
Requires:         R-tools 
Requires:         R-CRAN-Rcpp 

%description
Contains some functions catching all messages, 'stdout' and other useful
information while evaluating R code and other helpers to return user
specified text elements (like: header, paragraph, table, image, lists
etc.) in 'pandoc' markdown or several type of R objects similarly
automatically transformed to markdown format. Also capable of
exporting/converting (the resulting) complex 'pandoc' documents to e.g.
HTML, 'PDF', 'docx' or 'odt'. This latter reporting feature is supported
in brew syntax or with a custom reference class with a smarty caching
'backend'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
