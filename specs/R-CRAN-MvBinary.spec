%global __brp_check_rpaths %{nil}
%global packname  MvBinary
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Modelling Multivariate Binary Data with Blocks of SpecificOne-Factor Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-mgcv 
BuildRequires:    R-parallel 
Requires:         R-methods 
Requires:         R-mgcv 
Requires:         R-parallel 

%description
Modelling Multivariate Binary Data with Blocks of Specific One-Factor
Distribution. Variables are grouped into independent blocks. Each variable
is described by two continuous parameters (its marginal probability and
its dependency strength with the other block variables), and one binary
parameter (positive or negative dependency). Model selection consists in
the estimation of the repartition of the variables into blocks. It is
carried out by the maximization of the BIC criterion by a deterministic
(faster) algorithm or by a stochastic (more time consuming but optimal)
algorithm. Tool functions facilitate the model interpretation.

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
