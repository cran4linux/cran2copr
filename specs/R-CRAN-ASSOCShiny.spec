%global packname  ASSOCShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Document for Working with Association Rule MiningAnalysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-arulesViz 
BuildRequires:    R-CRAN-shinyMatrix 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-arulesViz 
Requires:         R-CRAN-shinyMatrix 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 

%description
An interactive document on the topic of association rule mining analysis
using 'rmarkdown' and 'shiny' packages. Runtime examples are provided in
the package function as well as at
<https://kartikeyabolar.shinyapps.io/ASSOCShiny/>.

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
%doc %{rlibdir}/%{packname}/ASSOCShiny.Rmd
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/K.jpg
%{rlibdir}/%{packname}/INDEX
