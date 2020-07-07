%global packname  blin
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}
Summary:          Bipartite Longitudinal Influence Network (BLIN) Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 

%description
Estimate influence networks from longitudinal bipartite relational data,
where the longitudinal relations are continuous. The outputs are estimates
of weighted influence networks among each actor type in the data set. The
generative model is the Bipartite Longitudinal Influence Network (BLIN)
model, a linear autoregressive model for these type of data. The
supporting paper is ``Inferring Influence Networks from Longitudinal
Bipartite Relational Data'', which is in preparation by the same authors.
The model may be estimated using maximum likelihood methods and Bayesian
methods. For more detail on methods, see Marrs et. al. <arXiv:1809.03439>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
