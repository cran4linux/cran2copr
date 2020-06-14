%global packname  samurais
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Statistical Models for the Unsupervised Segmentation ofTime-Series ('SaMUraiS')

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-MASS 
Requires:         R-CRAN-Rcpp 

%description
Provides a variety of original and flexible user-friendly statistical
latent variable models and unsupervised learning algorithms to segment and
represent time-series data (univariate or multivariate), and more
generally, longitudinal data, which include regime changes. 'samurais' is
built upon the following packages, each of them is an autonomous
time-series segmentation approach: Regression with Hidden Logistic Process
('RHLP'), Hidden Markov Model Regression ('HMMR'), Multivariate 'RHLP'
('MRHLP'), Multivariate 'HMMR' ('MHMMR'), Piece-Wise regression ('PWR').
For the advantages/differences of each of them, the user is referred to
our mentioned paper references.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
