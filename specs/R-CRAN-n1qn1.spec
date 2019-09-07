%global packname  n1qn1
%global packver   6.0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.1.3
Release:          1%{?dist}
Summary:          Port of the 'Scilab' 'n1qn1' and 'qnbd' Modules for(Un)constrained BFGS Optimization

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.5.600.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-Rcpp >= 0.12.3

%description
Provides 'Scilab' 'n1qn1', or Quasi-Newton BFGS "qn" without constraints
and 'qnbd' or Quasi-Newton BFGS with constraints. This takes more memory
than traditional L-BFGS.  The n1qn1 routine is useful since it allows
prespecification of a Hessian. If the Hessian is near enough the truth in
optimization it can speed up the optimization problem. Both algorithms are
described in the 'Scilab' optimization documentation located at
<http://www.scilab.org/content/download/250/1714/file/optimization_in_scilab.pdf>.

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
%doc %{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
