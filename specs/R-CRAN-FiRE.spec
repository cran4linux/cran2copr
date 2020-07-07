%global packname  FiRE
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}
Summary:          Finder of Rare Entities (FiRE)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-methods 

%description
The algorithm assigns rareness/ outlierness score to every sample in
voluminous datasets. The algorithm makes multiple estimations of the
proximity between a pair of samples, in low-dimensional spaces. To compute
proximity, FiRE uses Sketching, a variant of locality sensitive hashing.
For more details: Jindal, A., Gupta, P., Jayadeva and Sengupta, D., 2018.
Discovery of rare cells from voluminous single cell expression data.
Nature Communications, 9(1), p.4719. <doi:10.1038/s41467-018-07234-6>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
