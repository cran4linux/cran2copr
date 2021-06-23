%global __brp_check_rpaths %{nil}
%global packname  pkgdown
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Make Static HTML Documentation for a Package

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-callr >= 2.0.2
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-xml2 >= 1.3.1
BuildRequires:    R-CRAN-fs >= 1.3.0
BuildRequires:    R-CRAN-rmarkdown >= 1.1
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-downlit 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-callr >= 2.0.2
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-xml2 >= 1.3.1
Requires:         R-CRAN-fs >= 1.3.0
Requires:         R-CRAN-rmarkdown >= 1.1
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-downlit 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-rematch2 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-yaml 

%description
Generate an attractive and useful website from a source package. 'pkgdown'
converts your documentation, vignettes, 'README', and more to 'HTML'
making it easy to share information about your package online.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
