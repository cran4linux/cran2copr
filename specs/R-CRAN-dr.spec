%global packname  dr
%global packver   3.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.10
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Dimension Reduction for Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-graphics 

%description
Functions, methods, and datasets for fitting dimension reduction
regression, using slicing (methods SAVE and SIR), Principal Hessian
Directions (phd, using residuals and the response), and an iterative IRE.
Partial methods, that condition on categorical predictors are also
available.  A variety of tests, and stepwise deletion of predictors, is
also included.  Also included is code for computing permutation tests of
dimension.  Adding additional methods of estimating dimension is
straightforward. For documentation, see the vignette in the package.  With
version 3.0.4, the arguments for dr.step have been modified.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
