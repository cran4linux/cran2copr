%global __brp_check_rpaths %{nil}
%global packname  rpms
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          3%{?dist}%{?buildtag}
Summary:          Recursive Partitioning for Modeling Survey Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.3

%description
Functions to allow users to build and analyze design consistent tree and
random forest models using survey data from a complex sample design.  The
algorithm can fit a linear model to survey data in each node obtained by
recursively partitioning the data.  The splitting variables and selected
splits are obtained using a randomized permutation test procedure which
adjusted for complex sample design features used to obtain the data.
Likewise the model fitting algorithm produces design-consistent
coefficients to any specified least squares linear model between the
dependent and independent variables used in the end nodes. The main
functions return the resulting binary tree or random forest as an object
of "rpms" or "rpms_forest" type. The package also provides a number of
functions and methods available for use with these object types.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/News.html
%doc %{rlibdir}/%{packname}/News.md
%doc %{rlibdir}/%{packname}/notes
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
