%global __brp_check_rpaths %{nil}
%global packname  AutoStepwiseGLM
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Builds Stepwise GLMs via Train and Test Approach

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-formula.tools 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-formula.tools 

%description
Randomly splits data into testing and training sets. Then, uses stepwise
selection to fit numerous multiple regression models on the training data,
and tests them on the test data. Returned for each model are plots
comparing model Akaike Information Criterion (AIC), Pearson correlation
coefficient (r) between the predicted and actual values, Mean Absolute
Error (MAE), and R-Squared among the models. Each model is ranked relative
to the other models by the model evaluation metrics (i.e., AIC, r, MAE,
and R-Squared) and the model with the best mean ranking among the model
evaluation metrics is returned. Model evaluation metric weights for AIC,
r, MAE, and R-Squared are taken in as arguments as aic_wt, r_wt, mae_wt,
and r_squ_wt, respectively. They are equally weighted as default but may
be adjusted relative to each other if the user prefers one or more metrics
to the others, Field, A. (2013, ISBN:978-1-4462-4918-5).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
