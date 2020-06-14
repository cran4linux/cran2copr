%global packname  CVST
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Fast Cross-Validation via Sequential Testing

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-kernlab 
Requires:         R-Matrix 

%description
The fast cross-validation via sequential testing (CVST) procedure is an
improved cross-validation procedure which uses non-parametric testing
coupled with sequential analysis to determine the best parameter set on
linearly increasing subsets of the data. By eliminating under-performing
candidates quickly and keeping promising candidates as long as possible,
the method speeds up the computation while preserving the capability of a
full cross-validation. Additionally to the CVST the package contains an
implementation of the ordinary k-fold cross-validation with a flexible and
powerful set of helper objects and methods to handle the overall model
selection process. The implementations of the Cochran's Q test with
permutations and the sequential testing framework of Wald are generic and
can therefore also be used in other contexts.

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
%{rlibdir}/%{packname}/INDEX
