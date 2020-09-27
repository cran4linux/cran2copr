%global packname  packagefinder
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Comfortable Search for R Packages on CRAN, Either Directly from the R Console or with an R Studio Add-in

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tools >= 3.4.0
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-textutils 
BuildRequires:    R-CRAN-htmlTable 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinybusy 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-tools >= 3.4.0
Requires:         R-CRAN-httr 
Requires:         R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-textutils 
Requires:         R-CRAN-htmlTable 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinybusy 
Requires:         R-CRAN-rstudioapi 

%description
Search for R packages on CRAN directly from the R console, based on the
packages' titles, short and long descriptions, or other fields. Combine
multiple keywords with logical operators ('and', 'or'), view detailed
information on any package and keep track of the latest package
contributions to CRAN. If you don't want to search from the R console, use
the comfortable R Studio add-in.

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
