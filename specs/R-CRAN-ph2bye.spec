%global __brp_check_rpaths %{nil}
%global packname  ph2bye
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Phase II Clinical Trial Design Using Bayesian Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-animation 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-animation 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-VGAM 

%description
Calculate the Bayesian posterior/predictive probability and determine the
sample size and stopping boundaries for single-arm Phase II design.

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
