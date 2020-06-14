%global packname  muma
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          2%{?dist}
Summary:          Metabolomics Univariate and Multivariate Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-rrcov 
Requires:         R-CRAN-car 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-rrcov 

%description
Preprocessing of high-throughput data (normalization and scalings);
Principal Component Analysis with help tool for choosing best-separating
principal components and automatic testing for outliers; automatic
univariate analysis for parametric and non-parametric data, with
generation of specific reports (volcano and box plots); partial least
square discriminant analysis (PLS-DA); orthogonal partial least square
discriminant analysis (OPLS-DA); Statistical Total Correlation
Spectroscopy (STOCSY); Ratio Analysis Nuclear Magnetic Resonance (NMR)
Spectroscopy (RANSY).

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
