%global __brp_check_rpaths %{nil}
%global packname  vwr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Useful functions for visual word recognition research

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
Requires:         R-CRAN-stringdist 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 

%description
Functions and data for use in visual word recognition research:
Computation of neighbors (Hamming and Levenshtein distances), average
distances to neighbors (e.g., OLD20), and Coltheart's N. Also includes the
LD1NN algorithm to detect bias in the composition of a lexical decision
task. Most of the functions support parallel execution. Supplies wordlists
for several languages. Uses the string distance functions from the
stringdist package by Mark van der Loo.

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
