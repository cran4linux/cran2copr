%global packname  ICtest
%global packver   0.3-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          2%{?dist}
Summary:          Estimating and Testing the Number of Interesting Components inLinear Dimension Reduction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ICS >= 1.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-JADE 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ICSNP 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-ICS >= 1.3.0
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-JADE 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ICSNP 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-png 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-xts 

%description
For different linear dimension reduction methods like principal components
analysis (PCA), independent components analysis (ICA) and supervised
linear dimension reduction tests and estimates for the number of
interesting components (ICs) are provided.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
