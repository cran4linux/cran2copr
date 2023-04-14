%global __brp_check_rpaths %{nil}
%global packname  IndepTest
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Nonparametric Independence Tests Based on Entropy Estimation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rdpack 

%description
Implementations of the weighted Kozachenko-Leonenko entropy estimator and
independence tests based on this estimator, (Kozachenko and Leonenko
(1987) <http://mi.mathnet.ru/eng/ppi797>). Also includes a goodness-of-fit
test for a linear model which is an independence test between covariates
and errors.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
