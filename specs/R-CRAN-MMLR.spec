%global __brp_check_rpaths %{nil}
%global packname  MMLR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fitting Markov-Modulated Linear Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-pracma 

%description
A set of tools for fitting Markov-modulated linear regression, where
responses Y(t) are time-additive, and model operates in the external
environment, which is described as a continuous time Markov chain with
finite state space. Model is proposed by Alexander Andronov (2012)
<arXiv:1901.09600v1> and algorithm of parameters estimation is based on
eigenvalues and eigenvectors decomposition. Markov-switching regression
models have the same idea of varying the regression parameters randomly in
accordance with external environment. The difference is that for
Markov-modulated linear regression model the external environment is
described as a continuous-time homogeneous irreducible Markov chain with
known parameters while switching models consider Markov chain as
unobserved and estimation procedure involves estimation of transition
matrix. These models have significant differences in terms of the
analytical approach. Also, package provides a set of data simulation tools
for Markov-modulated linear regression (for academical/research purposes).
Research project No. 1.1.1.2/VIAA/1/16/075.

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
