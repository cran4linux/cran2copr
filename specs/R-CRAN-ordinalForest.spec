%global packname  ordinalForest
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          1%{?dist}
Summary:          Ordinal Forests: Prediction and Variable Ranking with OrdinalTarget Variables

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-verification 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-combinat 
Requires:         R-nnet 
Requires:         R-CRAN-verification 

%description
The ordinal forest (OF) method allows ordinal regression with
high-dimensional and low-dimensional data. After having constructed an OF
prediction rule using a training dataset, it can be used to predict the
values of the ordinal target variable for new observations. Moreover, by
means of the (permutation-based) variable importance measure of OF, it is
also possible to rank the covariates with respect to their importances in
the prediction of the values of the ordinal target variable. OF is
presented in Hornung (2020). NOTE: Starting with package version 2.4, it
is also possible to obtain class probability predictions in addition to
the class point predictions, where the variable importance values are also
obtained based on the class probabilities. The main functions of the
package are: ordfor() (construction of OF) and predict.ordfor()
(prediction of the target variable values of new observations).
References: Hornung R. (2020) Ordinal Forests. Journal of Classification
37, 4–17. <doi:10.1007/s00357-018-9302-x>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
