%global packname  mephas
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Shiny Application of Medical and Pharmaceutical Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-Rmisc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggfortify 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-plotROC 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-stargazer 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-spls 
BuildRequires:    R-CRAN-pls 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-Rmisc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggfortify 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-plotROC 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-stargazer 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-survminer 
Requires:         R-survival 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-spls 
Requires:         R-CRAN-pls 

%description
The web-based statistical fundamentals, tests, and models, aiming to
facilitate researchers to analyze medical, pharmaceutical and genomic
data.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
