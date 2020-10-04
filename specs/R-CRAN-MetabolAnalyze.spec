%global packname  MetabolAnalyze
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Probabilistic Latent Variable Models for Metabolomic Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-gplots 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-gplots 

%description
Fits probabilistic principal components analysis, probabilistic principal
components and covariates analysis and mixtures of probabilistic principal
components models to metabolomic spectral data.

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
%{rlibdir}/%{packname}/INDEX
