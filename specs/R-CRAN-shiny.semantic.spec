%global packname  shiny.semantic
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          'FomanticUI' Support for Shiny

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 0.8
BuildRequires:    R-CRAN-htmltools >= 0.2.6
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-shiny >= 0.12.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-htmlwidgets >= 0.8
Requires:         R-CRAN-htmltools >= 0.2.6
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-shiny >= 0.12.1
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-R6 

%description
Creating a great user interface for your Shiny apps can be a hassle,
especially if you want to work purely in R and don't want to use, for
instance HTML templates. This package adds support for a powerful UI
library 'FomanticUI' - <https://fomantic-ui.com/> (before: Semantic). It
also supports universal UI input binding that works with various DOM
elements.

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
