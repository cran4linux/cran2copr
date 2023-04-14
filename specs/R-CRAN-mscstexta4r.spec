%global __brp_check_rpaths %{nil}
%global packname  mscstexta4r
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          R Client for the Microsoft Cognitive Services Text AnalyticsREST API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-dplyr 
Requires:         R-utils 

%description
R Client for the Microsoft Cognitive Services Text Analytics REST API,
including Sentiment Analysis, Topic Detection, Language Detection, and Key
Phrase Extraction. An account MUST be registered at the Microsoft
Cognitive Services website <https://www.microsoft.com/cognitive-services/>
in order to obtain a (free) API key. Without an API key, this package will
not work properly.

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
