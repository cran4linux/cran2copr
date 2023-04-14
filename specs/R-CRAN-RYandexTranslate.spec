%global __brp_check_rpaths %{nil}
%global packname  RYandexTranslate
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          R Interface to Yandex Translate API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-jsonlite 

%description
'Yandex Translate' (https://translate.yandex.com/) is a statistical
machine translation system. The system translates separate words, complete
texts, and webpages. This package can be used to detect language from text
and to translate it to supported target language. For more info:
https://tech.yandex.com/translate/doc/dg/concepts/About-docpage/ .

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
