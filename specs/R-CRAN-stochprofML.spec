%global packname  stochprofML
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Stochastic Profiling using Maximum Likelihood Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0
Requires:         R-core >= 2.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-MASS 
Requires:         R-CRAN-numDeriv 

%description
This is an R package accompanying the paper "Parameterizing cell-to-cell
regulatory heterogeneities via stochastic transcriptional profiles" by
Sameer S Bajikar, Christiane Fuchs, Andreas Roller, Fabian J Theis and
Kevin A Janes (PNAS 2014, 111(5), E626-635). In this paper, we measure
expression profiles from small heterogeneous populations of cells, where
each cell is assumed to be from a mixture of lognormal distributions. We
perform maximum likelihood estimation in order to infer the mixture ratio
and the parameters of these lognormal distributions from the cumulated
expression measurements.

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
