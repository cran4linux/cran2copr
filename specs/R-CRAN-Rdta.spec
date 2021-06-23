%global __brp_check_rpaths %{nil}
%global packname  Rdta
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Data Transforming Augmentation for Linear Mixed Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MCMCpack >= 1.4.4
BuildRequires:    R-CRAN-mvtnorm >= 1.0.11
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
Requires:         R-CRAN-MCMCpack >= 1.4.4
Requires:         R-CRAN-mvtnorm >= 1.0.11
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
We provide a toolbox to fit univariate and multivariate linear mixed
models via data transforming augmentation. Users can also fit these models
via typical data augmentation for a comparison. It returns either maximum
likelihood estimates of unknown model parameters (hyper-parameters) via an
EM algorithm or posterior samples of those parameters via a Markov chain
Monte Carlo method. Also see Tak, You, Ghosh, Su, and Kelly (2019+)
<doi:10.1080/10618600.2019.1704295> <arXiv:1911.02748>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
