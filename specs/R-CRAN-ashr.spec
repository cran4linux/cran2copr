%global packname  ashr
%global packver   2.2-39
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.39
Release:          1%{?dist}
Summary:          Methods for Adaptive Shrinkage, using Empirical Bayes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.5
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-mixsqp 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-etrunct 
Requires:         R-CRAN-Rcpp >= 0.10.5
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-mixsqp 
Requires:         R-CRAN-SQUAREM 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-etrunct 

%description
The R package 'ashr' implements an Empirical Bayes approach for
large-scale hypothesis testing and false discovery rate (FDR) estimation
based on the methods proposed in M. Stephens, 2016, "False discovery
rates: a new deal", <DOI:10.1093/biostatistics/kxw041>. These methods can
be applied whenever two sets of summary statistics---estimated effects and
standard errors---are available, just as 'qvalue' can be applied to
previously computed p-values. Two main interfaces are provided: ash(),
which is more user-friendly; and ash.workhorse(), which has more options
and is geared toward advanced users. The ash() and ash.workhorse() also
provides a flexible modeling interface that can accomodate a variety of
likelihoods (e.g., normal, Poisson) and mixture priors (e.g., uniform,
normal).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
