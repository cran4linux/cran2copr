%global __brp_check_rpaths %{nil}
%global packname  qGaussian
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          3%{?dist}%{?buildtag}
Summary:          The q-Gaussian Distribution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-zipfR 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-stats 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-zipfR 

%description
Density, distribution function, quantile function and random generation
for the q-gaussian distribution with parameters mu and sig.

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
