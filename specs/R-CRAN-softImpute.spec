%global packname  softImpute
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Matrix Completion via Iterative Soft-Thresholded SVD

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Iterative methods for matrix completion that use nuclear-norm
regularization. There are two main approaches.The one approach uses
iterative soft-thresholded svds to impute the missing values. The second
approach uses alternating least squares. Both have an "EM" flavor, in that
at each iteration the matrix is completed with the current estimate. For
large matrices there is a special sparse-matrix class named "Incomplete"
that efficiently handles all computations. The package includes procedures
for centering and scaling rows, columns or both, and for computing
low-rank SVDs on large sparse centered matrices (i.e. principal
components)

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
