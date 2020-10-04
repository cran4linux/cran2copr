%global packname  mixggm
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Mixtures of Gaussian Graphical Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-mclust >= 5.4
BuildRequires:    R-CRAN-GA >= 3.1
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mclust >= 5.4
Requires:         R-CRAN-GA >= 3.1
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-network 
Requires:         R-CRAN-Rcpp 

%description
Mixtures of Gaussian graphical models for model-based clustering with
sparse covariance and concentration matrices. See Fop, Murphy, and Scrucca
(2018) <doi:10.1007/s11222-018-9838-y>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
