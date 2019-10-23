%global packname  parboost
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Distributed Model-Based Boosting

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-mboost 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-mboost 
Requires:         R-CRAN-party 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-doParallel 

%description
Distributed gradient boosting based on the mboost package. The parboost
package is designed to scale up component-wise functional gradient
boosting in a distributed memory environment by splitting the observations
into disjoint subsets, or alternatively using bootstrap samples (bagging).
Each cluster node then fits a boosting model to its subset of the data.
These boosting models are combined in an ensemble, either with equal
weights, or by fitting a (penalized) regression model on the predictions
of the individual models on the complete data.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
