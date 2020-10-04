%global packname  VarSelLCM
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Variable Selection for Model-Based Clustering of Mixed-Type DataSet with Missing Values

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-mgcv 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shiny 

%description
Full model selection (detection of the relevant features and estimation of
the number of clusters) for model-based clustering (see reference here
<doi:10.1007/s11222-016-9670-1>). Data to analyze can be continuous,
categorical, integer or mixed. Moreover, missing values can occur and do
not necessitate any pre-processing. Shiny application permits an easy
interpretation of the results.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/shinyApp
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
