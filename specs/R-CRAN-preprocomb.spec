%global packname  preprocomb
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Tools for Preprocessing Combinations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DMwR 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-clustertend 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-DMwR 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-clustertend 
Requires:         R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Preprocessing is often the most time-consuming phase in data analysis and
preprocessing transformations interdependent in unexpected ways. This
package helps to make preprocessing faster and more effective. It provides
an S4 framework for creating and evaluating preprocessing combinations for
classification, clustering and outlier detection. The framework supports
adding of user-defined preprocessors and preprocessing phases. Default
preprocessors can be used for low variance removal, missing value
imputation, scaling, outlier removal, noise smoothing, feature selection
and class imbalance correction.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
