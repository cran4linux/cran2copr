%global __brp_check_rpaths %{nil}
%global packname  dblr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Discrete Boosting Logistic Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-xgboost >= 0.6.4
BuildRequires:    R-CRAN-CatEncoders >= 0.1.1
BuildRequires:    R-CRAN-Metrics >= 0.1.1
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-xgboost >= 0.6.4
Requires:         R-CRAN-CatEncoders >= 0.1.1
Requires:         R-CRAN-Metrics >= 0.1.1
Requires:         R-methods 

%description
Trains logistic regression model by discretizing continuous variables via
gradient boosting approach. The proposed method tries to achieve a
tradeoff between interpretation and prediction accuracy for logistic
regression by discretizing the continuous variables. The variable binning
is accomplished in a supervised fashion. The model trained by this package
is still a single logistic regression model, but not a sequence of
logistic regression models. The fitted model object returned from the
model training consists of two tables. One table is used to give the
boundaries of bins for each continuous variable as well as the
corresponding coefficients, and the other one is used for discrete
variables. This package can also be used for binning continuous variables
for other statistical analysis.

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
%{rlibdir}/%{packname}/INDEX
