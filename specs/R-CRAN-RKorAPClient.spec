%global packname  RKorAPClient
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          'KorAP' Web Service Client Package

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R.cache 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-highcharter 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-keyring 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-PTXQC 
Requires:         R-CRAN-R.cache 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-highcharter 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-keyring 
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-PTXQC 

%description
A client package that makes the 'KorAP' web service API accessible from R.
The corpus analysis platform 'KorAP' has been developed as a scientific
tool to make potentially large, stratified and multiply annotated corpora,
such as the 'German Reference Corpus DeReKo' or the 'Corpus of the
Contemporary Romanian Language CoRoLa', accessible for linguists to let
them verify hypotheses and to find interesting patterns in real language
use. The 'RKorAPClient' package provides access to 'KorAP' and the corpora
behind it for user-created R code, as a programmatic alternative to the
'KorAP' web user-interface. You can learn more about 'KorAP' and use it
directly on 'DeReKo' at <https://korap.ids-mannheim.de/>.

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
