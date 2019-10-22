%global packname  STAT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Interactive Document for Working with Basic Statistical Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-psycho 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-corrgram 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-rpivotTable 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-datasets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-psycho 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-corrgram 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-rpivotTable 
Requires:         R-CRAN-psych 
Requires:         R-datasets 

%description
An interactive document on the topic of basic statistical analysis using
'rmarkdown' and 'shiny' packages. Runtime examples are provided in the
package function as well as at
<https://jarvisatharva.shinyapps.io/StatisticsPrimer/>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/K.jpg
%doc %{rlibdir}/%{packname}/STAT.Rmd
%{rlibdir}/%{packname}/INDEX
