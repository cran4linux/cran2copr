%global packname  minimaxdesign
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Minimax and Minimax Projection Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-DiceDesign 
BuildRequires:    R-CRAN-MaxPro 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-conf.design 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-DoE.base 
BuildRequires:    R-CRAN-FrF2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-DiceDesign 
Requires:         R-CRAN-MaxPro 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-conf.design 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-DoE.base 
Requires:         R-CRAN-FrF2 

%description
Provides two main functions, minimax() and miniMaxPro(), for computing
minimax and minimax projection designs using the minimax clustering
algorithm in Mak and Joseph (2018) <DOI:10.1080/10618600.2017.1302881>.
Current design region options include the unit hypercube ("hypercube"),
the unit simplex ("simplex"), the unit ball ("ball"), as well as
user-defined constraints on the unit hypercube ("custom"). Minimax designs
can also be computed on user-provided images using the function
minimax.map(). Design quality can be assessed using the function mMdist(),
which computes the minimax (fill) distance of a design.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
