%global __brp_check_rpaths %{nil}
%global packname  oncrawlR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Machine Learning for S.E.O

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.1
BuildRequires:    R-CRAN-RCurl >= 1.8
BuildRequires:    R-CRAN-e1071 >= 1.7
BuildRequires:    R-CRAN-jsonlite >= 1.6
BuildRequires:    R-CRAN-readr >= 1.3
BuildRequires:    R-CRAN-fs >= 1.3
BuildRequires:    R-CRAN-pROC >= 1.1
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-xgboost >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-pdp >= 0.7
BuildRequires:    R-CRAN-webshot >= 0.5
BuildRequires:    R-CRAN-rlist >= 0.4.6
BuildRequires:    R-CRAN-htmltools >= 0.3.5
BuildRequires:    R-CRAN-DALEX >= 0.3
BuildRequires:    R-CRAN-rlang >= 0.3
BuildRequires:    R-CRAN-rjson >= 0.2.20
BuildRequires:    R-CRAN-formattable >= 0.2
BuildRequires:    R-CRAN-sparkline >= 0.2
Requires:         R-CRAN-caret >= 6.0
Requires:         R-CRAN-ggplot2 >= 3.1
Requires:         R-CRAN-RCurl >= 1.8
Requires:         R-CRAN-e1071 >= 1.7
Requires:         R-CRAN-jsonlite >= 1.6
Requires:         R-CRAN-readr >= 1.3
Requires:         R-CRAN-fs >= 1.3
Requires:         R-CRAN-pROC >= 1.1
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-xgboost >= 0.8
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-pdp >= 0.7
Requires:         R-CRAN-webshot >= 0.5
Requires:         R-CRAN-rlist >= 0.4.6
Requires:         R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-DALEX >= 0.3
Requires:         R-CRAN-rlang >= 0.3
Requires:         R-CRAN-rjson >= 0.2.20
Requires:         R-CRAN-formattable >= 0.2
Requires:         R-CRAN-sparkline >= 0.2

%description
Measures different aspects of page content, structure and performance for
SEO (Search Engine Optimization). Aspects covered include HTML tags used
in SEO, duplicate and near-duplicate content, structured data, on-site
linking structure and popularity transfer, and many other amazing things.
This package can be used to generate a real, full SEO audit report, which
serves to detect errors or inefficiencies on a page that can be corrected
in order to optimise its performance on search engines.

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
