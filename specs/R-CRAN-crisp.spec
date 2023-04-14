%global __brp_check_rpaths %{nil}
%global packname  crisp
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fits a Model that Partitions the Covariate Space into Blocks ina Data- Adaptive Way

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Implements convex regression with interpretable sharp partitions (CRISP),
which considers the problem of predicting an outcome variable on the basis
of two covariates, using an interpretable yet non-additive model. CRISP
partitions the covariate space into blocks in a data-adaptive way, and
fits a mean model within each block. Unlike other partitioning methods,
CRISP is fit using a non-greedy approach by solving a convex optimization
problem, resulting in low-variance fits. More details are provided in
Petersen, A., Simon, N., and Witten, D. (2016). Convex Regression with
Interpretable Sharp Partitions. Journal of Machine Learning Research,
17(94): 1-31 <http://jmlr.org/papers/volume17/15-344/15-344.pdf>.

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
