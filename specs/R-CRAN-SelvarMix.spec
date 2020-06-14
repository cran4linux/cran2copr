%global packname  SelvarMix
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Regularization for Variable Selection in Model-Based Clusteringand Discriminant Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-Rmixmod 
BuildRequires:    R-parallel 
BuildRequires:    R-base 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-Rmixmod 
Requires:         R-parallel 
Requires:         R-base 
Requires:         R-methods 

%description
Performs a regularization approach to variable selection in the
model-based clustering and classification frameworks. First, the variables
are arranged in order with a lasso-like procedure. Second, the method of
Maugis, Celeux, and Martin-Magniette (2009, 2011)
<doi:10.1016/j.csda.2009.04.013>, <doi:10.1016/j.jmva.2011.05.004> is
adapted to define the role of variables in the two frameworks.

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
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
