%global packname  varbin
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Optimal Binning of Continuous and Categorical Variables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-rpart 
Requires:         R-rpart 

%description
Tool for easy and efficient discretization of continuous and categorical
data. The package calculates the most optimal binning of a given
explanatory variable with respect to a user-specified target variable. The
purpose is to assign a unique Weight-of-Evidence value to each of the
calculated binpoints in order to recode the original variable. The package
allows users to impose certain restrictions on the functional form on the
resulting binning while maximizing the overall information value in the
original data. The package is well suited for logistic scoring models
where input variables may be subject to restrictions such as linearity by
e.g. regulatory authorities. An excellent source describing in detail the
development of scorecards, and the role of Weight-of-Evidence coding in
credit scoring is (Siddiqi 2006, ISBN: 978–0-471–75451–0). The package
utilizes the discrete nature of decision trees and Isotonic Regression to
accommodate the trade-off between flexible functional forms and maximum
information value.

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
%{rlibdir}/%{packname}/INDEX
