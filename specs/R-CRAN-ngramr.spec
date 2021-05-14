%global packname  ngramr
%global packver   1.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.4
Release:          1%{?dist}%{?buildtag}
Summary:          Retrieve and Plot Google n-Gram Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.3
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-textutils 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-dplyr >= 1.0.3
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-textutils 
Requires:         R-CRAN-lifecycle 

%description
Retrieve and plot word frequencies through time from the "Google Ngram
Viewer" <https://books.google.com/ngrams>.

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
