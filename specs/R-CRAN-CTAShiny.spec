%global packname  CTAShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Interactive Application for Working with Contingency Tables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyMatrix 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-rpivotTable 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyMatrix 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-rpivotTable 

%description
An interactive application for working with contingency Tables. The
application has a template for solving contingency table problems like
chisquare test of independence,association plot between two categorical
variables. Runtime examples are provided in the package function as well
as at <https://jarvisatharva.shinyapps.io/CategoricalDataAnalysis/>.

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
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
