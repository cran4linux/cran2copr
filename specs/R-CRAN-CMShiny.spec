%global packname  CMShiny
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Document for Working with Confusion Matrix

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-shinyMatrix 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-epitools 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-shinyMatrix 
Requires:         R-Matrix 
Requires:         R-CRAN-epitools 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-e1071 

%description
An interactive document on the topic of confusion matrix analysis using
'rmarkdown' and 'shiny' packages. Runtime examples are provided in the
package function as well as at
<https://predanalyticssessions1.shinyapps.io/ConfusionMatrixShiny/>.

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
%doc %{rlibdir}/%{packname}/CMShiny.Rmd
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/K.jpg
%{rlibdir}/%{packname}/INDEX
