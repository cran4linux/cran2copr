%global packname  bsplus
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          2%{?dist}%{?buildtag}
Summary:          Adds Functionality to the R Markdown + Shiny Bootstrap Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-methods 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-jsonlite 

%description
The Bootstrap framework lets you add some JavaScript functionality to your
web site by adding attributes to your HTML tags - Bootstrap takes care of
the JavaScript <https://getbootstrap.com/javascript>. If you are using R
Markdown or Shiny, you can use these functions to create collapsible
sections, accordion panels, modals, tooltips, popovers, and an accordion
sidebar framework (not described at Bootstrap site).

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
