%global packname  insee
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools to Easily Download Data from INSEE BDM Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-readsdmx 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-openssl 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-readsdmx 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-openssl 

%description
Using embedded sdmx queries, get the data of more than 150 000 insee
series from bdm database. Have a look at the detailed sdmx web service
page with the following link :
<https://www.insee.fr/en/information/2868055>.

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
