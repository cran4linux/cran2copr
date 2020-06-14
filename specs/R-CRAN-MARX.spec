%global packname  MARX
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          2%{?dist}
Summary:          Simulation, Estimation, Model Selection and Forecasting for MARXModels

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-stabledist 
BuildRequires:    R-CRAN-metRology 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-fBasics 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-stabledist 
Requires:         R-CRAN-metRology 

%description
Simulate, estimate (by t-MLE), select and forecast mixed causal-noncausal
autoregressive models with possibly exogenous regressors, using methods
proposed in Lanne and Saikkonen (2011) <doi:10.2202/1941-1928.1080> and
Hecq et al. (2016) <doi:10.15609/annaeconstat2009.123-124.0307>.

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
