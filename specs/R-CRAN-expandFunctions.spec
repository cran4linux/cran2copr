%global __brp_check_rpaths %{nil}
%global packname  expandFunctions
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Feature Matrix Builder

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-orthopolynom 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-orthopolynom 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-glmnet 

%description
Generates feature matrix outputs from R object inputs using a variety of
expansion functions.  The generated feature matrices have applications as
inputs for a variety of machine learning algorithms. The expansion
functions are based on coercing the input to a matrix, treating the
columns as features and converting individual columns or combinations into
blocks of columns. Currently these include expansion of columns by
efficient sparse embedding by vectors of lags, quadratic expansion into
squares and unique products, powers by vectors of degree, vectors of
orthogonal polynomials functions, and block random affine projection
transformations (RAPTs). The transformations are magrittr- and
cbind-friendly, and can be used in a building block fashion.  For
instance, taking the cos() of the output of the RAPT transformation
generates a stationary kernel expansion via Bochner's theorem, and this
expansion can then be cbind-ed with other features. Additionally, there
are utilities for replacing features, removing rows with NAs, creating
matrix samples of a given distribution, a simple wrapper for LASSO with
CV, a Freeman-Tukey transform, generalizations of the outer function,
matrix size-preserving discrete difference by row, plotting, etc.

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
