%global __brp_check_rpaths %{nil}
%global packname  ph2bayes
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Single-Arm Phase II Designs

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-stats 

%description
An implementation of Bayesian single-arm phase II design methods for
binary outcome based on posterior probability (Thall and Simon (1994)
<doi:10.2307/2533377>) and predictive probability (Lee and Liu (2008)
<doi:10.1177/1740774508089279>).

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
