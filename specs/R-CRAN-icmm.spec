%global packname  icmm
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Empirical Bayes Variable Selection via ICM/M Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EbayesThresh 
Requires:         R-CRAN-EbayesThresh 

%description
Carries out empirical Bayes variable selection via ICM/M algorithm. The
basic problem is to fit high-dimensional regression which most
coefficients are assumed to be zero. This package allows incorporating the
Ising prior to capture structure of predictors in the modeling process.
The current version of this package can handle the normal, binary
logistic, and Cox's regression (Pungpapong et. al. (2015)
<doi:10.1214/15-EJS1034>, Pungpapong et. al. (2017) <arXiv:1707.08298>).

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
