%global packname  flare
%global packver   1.6.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0.2
Release:          1%{?dist}
Summary:          Family of Lasso Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-methods 

%description
Provide the implementation of a family of Lasso variants including Dantzig
Selector, LAD Lasso, SQRT Lasso, Lq Lasso for estimating high dimensional
sparse linear model. We adopt the alternating direction method of
multipliers and convert the original optimization problem into a
sequential L1 penalized least square minimization problem, which can be
efficiently solved by linearization algorithm. A multi-stage screening
approach is adopted for further acceleration. Besides the sparse linear
model estimation, we also provide the extension of these Lasso variants to
sparse Gaussian graphical model estimation including TIGER and CLIME using
either L1 or adaptive penalty. Missing values can be tolerated for Dantzig
selector and CLIME. The computation is memory-optimized using the sparse
matrix output.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
