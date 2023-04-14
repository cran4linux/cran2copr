%global __brp_check_rpaths %{nil}
%global packname  DetMCD
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation of the DetMCD Algorithm (Robust and DeterministicEstimation of Location and Scatter)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-pcaPP 

%description
Implementation of DetMCD, a new algorithm for robust and deterministic
estimation of location and scatter. The benefits of robust and
deterministic estimation are explained in Hubert, Rousseeuw and Verdonck
(2012) <doi:10.1080/10618600.2012.672100>.

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
