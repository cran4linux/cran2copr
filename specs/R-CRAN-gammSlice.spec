%global packname  gammSlice
%global packver   2.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Additive Mixed Model Analysis via Slice Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-KernSmooth 
BuildRequires:    R-lattice 
BuildRequires:    R-mgcv 
Requires:         R-KernSmooth 
Requires:         R-lattice 
Requires:         R-mgcv 

%description
Uses a slice sampling-based Markov chain Monte Carlo to conduct Bayesian
fitting and inference for generalized additive mixed models.  Generalized
linear mixed models and generalized additive models are also handled as
special cases of generalized additive mixed models. The methodology and
software is described in Pham, T.H. and Wand, M.P. (2018). Australian and
New Zealand Journal of Statistics, 60, 279-330 <DOI:10.1111/ANZS.12241>.

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
%{rlibdir}/%{packname}/libs
