%global packname  RfEmpImp
%global packver   2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.3
Release:          1%{?dist}
Summary:          Multiple Imputation using Chained Random Forests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mice >= 3.8.0
BuildRequires:    R-CRAN-ranger >= 0.12.1
Requires:         R-CRAN-mice >= 3.8.0
Requires:         R-CRAN-ranger >= 0.12.1

%description
Functions for methods for multiple imputation using chained random
forests. Implemented algorithms can handle missing data in both continuous
and categorical variables by using prediction-based or node-based
conditional distributions constructed using random forests. For
prediction-based imputation, the method based on the empirical
distribution of out-of-bag prediction errors of random forests and the
method based on normality assumption are provided. For node-based
imputation, the method based on the conditional distribution formed by
predicting nodes of random forests and the method based on measures of
proximities of random forests are provided. More details of the
statistical methods can be found in Hong et al. (2020) <arXiv:2004.14823>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
