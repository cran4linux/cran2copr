%global packname  nsga3
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          2%{?dist}
Summary:          An Implementation of Non-Dominated Sorting Genetic Algorithm IIIfor Feature Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-CRAN-rPref 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-parallelMap 
Requires:         R-CRAN-rPref 
Requires:         R-CRAN-xgboost 

%description
An adaptation of Non-dominated Sorting Genetic Algorithm III for multi
objective feature selection tasks. Non-dominated Sorting Genetic Algorithm
III is a genetic algorithm that solves multiple optimization problems
simultaneously by applying a non-dominated sorting technique. It uses a
reference points based selection operator to explore solution space and
preserve diversity. See the original paper by K. Deb and H. Jain (2014)
<DOI:10.1109/TEVC.2013.2281534> for a detailed description.

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
