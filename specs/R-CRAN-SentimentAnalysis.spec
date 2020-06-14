%global packname  SentimentAnalysis
%global packver   1.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          2%{?dist}
Summary:          Dictionary-Based Sentiment Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-spikeslab >= 1.1
BuildRequires:    R-CRAN-tm >= 0.6
BuildRequires:    R-CRAN-ngramrr >= 0.1
BuildRequires:    R-CRAN-qdapDictionaries 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-spikeslab >= 1.1
Requires:         R-CRAN-tm >= 0.6
Requires:         R-CRAN-ngramrr >= 0.1
Requires:         R-CRAN-qdapDictionaries 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 

%description
Performs a sentiment analysis of textual contents in R. This
implementation utilizes various existing dictionaries, such as Harvard IV,
or finance-specific dictionaries. Furthermore, it can also create
customized dictionaries. The latter uses LASSO regularization as a
statistical approach to select relevant terms based on an exogenous
response variable.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
