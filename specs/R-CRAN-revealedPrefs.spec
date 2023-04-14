%global __brp_check_rpaths %{nil}
%global packname  revealedPrefs
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Revealed Preferences and Microeconomic Rationality

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pso 

%description
Computation of (direct and indirect) revealed preferences, fast
non-parametric tests of rationality axioms (WARP, SARP, GARP), simulation
of axiom-consistent data, and detection of axiom-consistent
subpopulations. Rationality tests follow Varian (1982)
<doi:10.2307/1912771>, axiom-consistent subpopulations follow Crawford and
Pendakur (2012) <doi:10.1111/j.1468-0297.2012.02545.x>.

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
