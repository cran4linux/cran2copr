%global packname  polyreg
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}
Summary:          Polynomial Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-dummies 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-partools 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-nnet 
Requires:         R-CRAN-dummies 
Requires:         R-parallel 
Requires:         R-CRAN-partools 
Requires:         R-CRAN-RSpectra 
Requires:         R-stats 
Requires:         R-utils 

%description
Automate formation and evaluation of polynomial regression models.
Provides support for cross-validating categorical variables. The
motivation for this package is described in 'Polynomial Regression As an
Alternative to Neural Nets' by Xi Cheng, Bohdan Khomtchouk, Norman
Matloff, and Pete Mohanty (<arXiv:1806.06850>).

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
%{rlibdir}/%{packname}/INDEX
