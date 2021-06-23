%global __brp_check_rpaths %{nil}
%global packname  eMLEloglin
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Fitting log-Linear Models in Sparse Contingency Tables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolveAPI 
Requires:         R-CRAN-lpSolveAPI 

%description
Log-linear modeling is a popular method for the analysis of contingency
table data. When the table is sparse, the data can fall on the boundary of
the convex support, and we say that "the MLE does not exist" in the sense
that some parameters cannot be estimated. However, an extended MLE always
exists, and a subset of the original parameters will be estimable. The
'eMLEloglin' package determines which sampling zeros contribute to the
non-existence of the MLE. These problematic zero cells can be removed from
the contingency table and the model can then be fit (as far as is
possible) using the glm() function.

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
