%global packname  rtmpt
%global packver   0.1-18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.18
Release:          1%{?dist}
Summary:          Fitting RT-MPT Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-loo 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-utils 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-loo 
Requires:         R-CRAN-matrixcalc 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-truncnorm 
Requires:         R-utils 

%description
Fit response-time extended multinomial processing tree (RT-MPT) models by
Klauer and Kellen (2018) <doi:10.1016/j.jmp.2017.12.003>. The RT-MPT class
not only incorporate frequencies like traditional multinomial processing
tree (MPT) models, but also latencies. This enables it to estimate process
completion times and encoding plus motor execution times next to the
process probabilities of traditional MPTs. 'rtmpt' is a Bayesian framework
and posterior samples are sampled using a Metropolis-Gibbs sampler like
the one described in the Klauer and Kellen (2018), but with some
modifications. Other than in the original C++ program we use the free and
open source GNU Scientific Library (GSL). There is also the possibility to
suppress single process completion times.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
