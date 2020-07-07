%global packname  fad
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Factor Analysis for Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-Matrix >= 1.1.0
BuildRequires:    R-CRAN-RSpectra >= 0.16.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-methods 
Requires:         R-Matrix >= 1.1.0
Requires:         R-CRAN-RSpectra >= 0.16.0
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-methods 

%description
Compute maximum likelihood estimators of parameters in a Gaussian factor
model using the the matrix-free methodology described in Dai et al. (2019)
<doi:10.1080/10618600.2019.1704296>. In contrast to the factanal()
function from 'stats' package, fad() can handle high-dimensional datasets
where number of variables exceed the sample size and is also substantially
faster than the EM algorithms.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
