%global packname  PROBShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Interactive Document for Working with Basic Probability

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-shinyMatrix 
BuildRequires:    R-CRAN-rpivotTable 
BuildRequires:    R-CRAN-epitools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-shinyMatrix 
Requires:         R-CRAN-rpivotTable 
Requires:         R-CRAN-epitools 

%description
An interactive document on the topic of basic probability using
'rmarkdown' and 'shiny' packages. Runtime examples are provided in the
package function as well as at
<https://analyticmodels.shinyapps.io/BayesShiny/>.

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
%doc %{rlibdir}/%{packname}/PROBShiny.Rmd
%{rlibdir}/%{packname}/INDEX
