%global packname  SEL
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Semiparametric elicitation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-lattice 
Requires:         R-splines 
Requires:         R-CRAN-quadprog 
Requires:         R-lattice 

%description
This package implements a novel method for fitting a bounded probability
distribution to quantiles (for example stated by an expert), see Bornkamp
and Ickstadt (2009) for details.  For this purpose B-splines are used, and
the density is obtained by penalized least squares based on a Brier
entropy penalty.  The package provides methods for fitting the
distribution as well as methods for evaluating the underlying density and
cdf. In addition methods for plotting the distribution, drawing random
numbers and calculating quantiles of the obtained distribution are
provided.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
