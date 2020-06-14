%global packname  StratifiedRF
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Builds Trees by Sampling Variables in Groups

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-dplyr 
Requires:         R-parallel 
Requires:         R-stats 

%description
Random Forest-like tree ensemble that works with groups of predictor
variables. When building a tree, a number of variables is taken randomly
from each group separately, thus ensuring that it considers variables from
each group for the splits. Useful when rows contain information about
different things (e.g. user information and product information) and it's
not sensible to make a prediction with information from only one group of
variables, or when there are far more variables from one group than the
other and it's desired to have groups appear evenly on trees. Trees are
grown using the C5.0 algorithm rather than the usual CART algorithm.
Supports parallelization (multithreaded), missing values in predictors,
and categorical variables (without doing One-Hot encoding in the
processing). Can also be used to create a regular (non-stratified) Random
Forest-like model, but made up of C5.0 trees and with some additional
control options. As it's built with C5.0 trees, it works only for
classification (not for regression).

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
