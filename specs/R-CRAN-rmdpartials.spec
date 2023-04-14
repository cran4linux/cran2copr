%global __brp_check_rpaths %{nil}
%global packname  rmdpartials
%global packver   0.5.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.8
Release:          3%{?dist}%{?buildtag}
Summary:          Partial 'rmarkdown' Documents to Prettify your Reports

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-digest 
Requires:         R-utils 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rlang 

%description
Use 'rmarkdown' partials, also know as child documents in 'knitr', so you
can make components for HTML, PDF, and Word documents. The package
provides various helper functions to make certain functions easier. You
may want to use this package, if you want to flexibly summarise objects
using a combination of figures, tables, text, and HTML widgets. Unlike
HTML widgets, the output is Markdown and can hence be turn into other
output formats than HTML.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
