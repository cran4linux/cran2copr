%global packname  robust
%global packver   0.5-0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0.0
Release:          1%{?dist}
Summary:          Port of the S+ "Robust Library"

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-fit.models 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-rrcov 
Requires:         R-CRAN-fit.models 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-rrcov 

%description
Methods for robust statistics, a state of the art in the early 2000s,
notably for robust regression and robust multivariate analysis.

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
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/datasets
%doc %{rlibdir}/%{packname}/tests_S
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
