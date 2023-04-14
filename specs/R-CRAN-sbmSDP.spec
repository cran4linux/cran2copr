%global __brp_check_rpaths %{nil}
%global packname  sbmSDP
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Semidefinite Programming for Fitting Block Models of Equal BlockSizes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.6
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.6

%description
An ADMM implementation of SDP-1, a semidefinite programming relaxation of
the maximum likelihood estimator for fitting a block model. SDP-1 has a
tendency to produce equal-sized blocks and is ideal for producing a form
of network histogram approximating a nonparametric graphon model.
Alternatively, it can be used for community detection. (This is
experimental code, proceed with caution.)

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
