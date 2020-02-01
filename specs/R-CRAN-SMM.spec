%global packname  SMM
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Simulation and Estimation of Multi-State Discrete-TimeSemi-Markov and Markov Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-DiscreteWeibull 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-DiscreteWeibull 

%description
Performs parametric and non-parametric estimation and simulation for
multi-state discrete-time semi-Markov processes. For the parametric
estimation, several discrete distributions are considered for the sojourn
times: Uniform, Geometric, Poisson, Discrete Weibull and Negative
Binomial. The non-parametric estimation concerns the sojourn time
distributions, where no assumptions are done on the shape of
distributions. Moreover, the estimation can be done on the basis of one or
several sample paths, with or without censoring at the beginning or/and at
the end of the sample paths. The implemented methods are described in
Barbu, V.S., Limnios, N. (2008) <doi:10.1007/978-0-387-73173-5>, Barbu,
V.S., Limnios, N. (2008) <doi:10.1080/10485250701261913> and Trevezas, S.,
Limnios, N. (2011) <doi:10.1080/10485252.2011.555543>. Estimation and
simulation of discrete-time k-th order Markov chains are also considered.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
