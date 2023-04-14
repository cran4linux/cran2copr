%global __brp_check_rpaths %{nil}
%global packname  sobolnp
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Nonparametric Sobol Estimator with Bootstrap Bandwidth

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-pbmcapply 
Requires:         R-CRAN-np 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-pbmcapply 

%description
Algorithm to estimate the Sobol indices using a non-parametric fit of the
regression curve. The bandwidth is estimated using bootstrap to reduce the
finite-sample bias. The package is based on the paper Solís, M. (2018)
<arXiv:1803.03333>.

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
