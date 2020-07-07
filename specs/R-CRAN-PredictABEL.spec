%global packname  PredictABEL
%global packver   1.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          3%{?dist}
Summary:          Assessment of Risk Prediction Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-PBSmodelling 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-methods 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-PBSmodelling 
Requires:         R-CRAN-lazyeval 
Requires:         R-methods 

%description
We included functions to assess the performance of risk models. The
package contains functions for the various measures that are used in
empirical studies, including univariate and multivariate odds ratios (OR)
of the predictors, the c-statistic (or area under the receiver operating
characteristic (ROC) curve (AUC)), Hosmer-Lemeshow goodness of fit test,
reclassification table, net reclassification improvement (NRI) and
integrated discrimination improvement (IDI). Also included are functions
to create plots, such as risk distributions, ROC curves, calibration plot,
discrimination box plot and predictiveness curves. In addition to
functions to assess the performance of risk models, the package includes
functions to obtain weighted and unweighted risk scores as well as
predicted risks using logistic regression analysis. These logistic
regression functions are specifically written for models that include
genetic variables, but they can also be applied to models that are based
on non-genetic risk factors only. Finally, the package includes function
to construct a simulated dataset with genotypes, genetic risks, and
disease status for a hypothetical population, which is used for the
evaluation of genetic risk models.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
