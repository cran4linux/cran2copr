%global packname  vosonSML
%global packver   0.29.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.29.4
Release:          1%{?dist}
Summary:          Collecting Social Media Data and Generating Networks forAnalysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RedditExtractoR >= 2.1.2
BuildRequires:    R-CRAN-igraph >= 1.2.2
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-rtweet >= 0.6.8
BuildRequires:    R-CRAN-rlang >= 0.3.0.1
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-textutils 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-RedditExtractoR >= 2.1.2
Requires:         R-CRAN-igraph >= 1.2.2
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-rtweet >= 0.6.8
Requires:         R-CRAN-rlang >= 0.3.0.1
Requires:         R-CRAN-tm 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-httpuv 
Requires:         R-methods 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-textutils 
Requires:         R-CRAN-tictoc 
Requires:         R-stats 
Requires:         R-CRAN-purrr 

%description
A suite of tools for collecting and constructing networks from social
media data. Provides easy-to-use functions for collecting data across
popular platforms (Twitter, YouTube and Reddit) and generating different
types of networks for analysis.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
