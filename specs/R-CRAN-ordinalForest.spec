%global packname  ordinalForest
%global packver   2.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Ordinal Forests: Prediction and Variable Ranking with OrdinalTarget Variables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-nnet 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-ggplot2 
Requires:         R-nnet 

%description
The ordinal forest (OF) method allows ordinal regression with
high-dimensional and low-dimensional data. After having constructed an OF
prediction rule using a training dataset, it can be used to predict the
values of the ordinal target variable for new observations. Moreover, by
means of the (permutation-based) variable importance measure of OF, it is
also possible to rank the covariates with respect to their importances in
the prediction of the values of the ordinal target variable. OF is
presented in Hornung (2019). The main functions of the package are:
ordfor() (construction of OF) and predict.ordfor() (prediction of the
target variable values of new observations). References: Hornung R. (2019)
Ordinal Forests. Journal of Classification,
<doi:10.1007/s00357-018-9302-x>.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
