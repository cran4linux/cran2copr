%global packname  LAM
%global packver   0.5-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.15
Release:          2%{?dist}
Summary:          Some Latent Variable Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-CDM 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-sirt 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CDM 
Requires:         R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-sirt 
Requires:         R-stats 
Requires:         R-utils 

%description
Includes some procedures for latent variable modeling with a particular
focus on multilevel data. The 'LAM' package contains mean and covariance
structure modelling for multivariate normally distributed data
(mlnormal(); Longford, 1987; <doi:10.1093/biomet/74.4.817>), a general
Metropolis-Hastings algorithm (amh(); Roberts & Rosenthal, 2001,
<doi:10.1214/ss/1015346320>) and penalized maximum likelihood estimation
(pmle(); Cole, Chu & Greenland, 2014; <doi:10.1093/aje/kwt245>).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
