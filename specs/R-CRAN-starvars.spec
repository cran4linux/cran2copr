%global packname  starvars
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          2%{?dist}
Summary:          Vector Logistic Smooth Transition Models / Realized CovariancesConstruction

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-vars 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-highfrequency 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-lessR 
BuildRequires:    R-CRAN-quantmod 
Requires:         R-MASS 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-vars 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-rlist 
Requires:         R-stats4 
Requires:         R-CRAN-highfrequency 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-lessR 
Requires:         R-CRAN-quantmod 

%description
Allows the user to estimate a vector logistic smooth transition
autoregressive model via maximum log-likelihood or nonlinear least
squares. It further permits to test for linearity in the multivariate
framework against a vector logistic smooth transition autoregressive model
with a single transition variable. The estimation method is discussed in
Terasvirta and Yang (2014, <doi:10.1108/S0731-9053(2013)0000031008>).
Also, realized covariances can be constructed from stock market prices or
returns, as explained in Andersen et al. (2001,
<doi:10.1016/S0304-405X(01)00055-1>).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
