%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  juicedown
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          'juice' + 'markdown': Convert 'R Markdown' into 'HTML' with Inline Styles

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-juicyjuice 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-sass 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-juicyjuice 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-sass 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-xml2 

%description
A convenience tool to create 'HTML' with inline styles using 'juicyjuice'
and 'markdown' packages. It is particularly useful when working on a
content management system (CMS) whose code editor eliminates style and
link tags. The main use case of the package is the learning management
system, 'Moodle'. Additional helper functions for teaching purposes are
provided. Learn more about 'juicedown' at
<https://kenjisato.github.io/juicedown/>.

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
