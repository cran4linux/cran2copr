%global packname  xgboost
%global packver   1.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}
Summary:          Extreme Gradient Boosting

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-Matrix >= 1.1.0
BuildRequires:    R-CRAN-stringi >= 0.5.2
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-Matrix >= 1.1.0
Requires:         R-CRAN-stringi >= 0.5.2
Requires:         R-methods 

%description
Extreme Gradient Boosting, which is an efficient implementation of the
gradient boosting framework from Chen & Guestrin (2016)
<doi:10.1145/2939672.2939785>. This package is its R interface. The
package includes efficient linear model solver and tree learning
algorithms. The package can automatically do parallel computation on a
single machine which could be more than 10 times faster than existing
gradient boosting packages. It supports various objective functions,
including regression, classification and ranking. The package is made to
be extensible, so that users are also allowed to define their own
objectives easily.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
