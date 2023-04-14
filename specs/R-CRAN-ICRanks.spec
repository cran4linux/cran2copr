%global __brp_check_rpaths %{nil}
%global packname  ICRanks
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Simultaneous Confidence Intervals for Ranks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.11
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-gmp 
Requires:         R-CRAN-Rcpp >= 0.12.11
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-gmp 

%description
Algorithms to construct simultaneous confidence intervals for the ranks of
means mu_1,...,mu_n based on an independent Gaussian sample using multiple
testing techniques.

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
