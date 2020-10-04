%global packname  OSNMTF
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Orthogonal Sparse Non-Negative Matrix Tri-Factorization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.4
Requires:         R-core >= 3.4.4
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-MASS 
Requires:         R-stats 

%description
A novel method to implement cancer subtyping and subtype specific drug
targets identification via non-negative matrix tri-factorization. To
improve the interpretability, we introduce orthogonal constraint to the
row coefficient matrix and column coefficient matrix. To meet the prior
knowledge that each subtype should be strongly associated with few gene
sets, we introduce sparsity constraint to the association sub-matrix. The
average residue was introduced to evaluate the row and column cluster
numbers. This is part of the work "Liver Cancer Analysis via Orthogonal
Sparse Non-Negative Matrix Tri- Factorization" which will be submitted to
BBRC.

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
