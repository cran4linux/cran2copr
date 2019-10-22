%global packname  NNS
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          1%{?dist}
Summary:          Nonlinear Nonparametric Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-stringr 

%description
Nonlinear nonparametric statistics using partial moments.  Partial moments
are the elements of variance and asymptotically approximate the area of
f(x).  These robust statistics provide the basis for nonlinear analysis
while retaining linear equivalences.  NNS offers: Numerical integration,
Numerical differentiation, Clustering, Correlation, Dependence, Causal
analysis, ANOVA, Regression, Classification, Seasonality, Autoregressive
modeling, Normalization and Stochastic dominance.  All routines based on:
Viole, F. and Nawrocki, D. (2013), Nonlinear Nonparametric Statistics:
Using Partial Moments (ISBN: 1490523995).

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
