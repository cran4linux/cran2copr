%global packname  semsfa
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Semiparametric Estimation of Stochastic Frontier Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-iterators 
Requires:         R-mgcv 
Requires:         R-CRAN-np 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-iterators 

%description
Semiparametric Estimation of Stochastic Frontier Models following a two
step procedure: in the first step semiparametric or nonparametric
regression techniques are used to relax parametric restrictions of the
functional form representing technology and in the second step variance
parameters are obtained by pseudolikelihood estimators or by method of
moments.

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
