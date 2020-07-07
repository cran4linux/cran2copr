%global packname  lmviz
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          A Package to Visualize Linear Models Features and Play with Them

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-mgcv 
BuildRequires:    R-methods 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-lmtest 
Requires:         R-mgcv 
Requires:         R-methods 

%description
Contains three shiny applications. Two are meant to explore linear model
inference feature through simulation. The third is a game to learn
interpreting diagnostic plots.

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
%doc %{rlibdir}/%{packname}/BadLMApp.r
%doc %{rlibdir}/%{packname}/images
%license %{rlibdir}/%{packname}/LICENSEMEDIA
%doc %{rlibdir}/%{packname}/QuizResidualApp.r
%doc %{rlibdir}/%{packname}/SimpleLMApp.r
%doc %{rlibdir}/%{packname}/sounds
%{rlibdir}/%{packname}/INDEX
