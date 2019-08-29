%global packname  MNLR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Interactive Shiny Presentation for Working with MultinomialLogistic Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-datasets 
BuildRequires:    R-stats 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 
Requires:         R-nnet 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-caret 
Requires:         R-datasets 
Requires:         R-stats 

%description
An interactive presentation on the topic of Multinomial Logistic
Regression. It is helpful to those who want to learn Multinomial Logistic
Regression quickly and get a hands on experience. The presentation has a
template for solving problems on Multinomial Logistic Regression. Runtime
examples are provided in the package function as well as at
<https://jarvisatharva.shinyapps.io/MultinomPresentation>.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/IA.jpg
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/IRIS.jpg
%doc %{rlibdir}/%{packname}/K.jpg
%doc %{rlibdir}/%{packname}/M.Rmd
%doc %{rlibdir}/%{packname}/MC.csv
%doc %{rlibdir}/%{packname}/MP.jpg
%doc %{rlibdir}/%{packname}/multinom.txt
%doc %{rlibdir}/%{packname}/PW.jpg
%doc %{rlibdir}/%{packname}/RS.jpg
%doc %{rlibdir}/%{packname}/VC.jpg
%{rlibdir}/%{packname}/INDEX
