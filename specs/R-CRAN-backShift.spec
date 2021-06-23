%global __brp_check_rpaths %{nil}
%global packname  backShift
%global packver   0.1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4.3
Release:          3%{?dist}%{?buildtag}
Summary:          Learning Causal Cyclic Graphs from Unknown Shift Interventions

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 

%description
Code for 'backShift', an algorithm to estimate the connectivity matrix of
a directed (possibly cyclic) graph with hidden variables. The underlying
system is required to be linear and we assume that observations under
different shift interventions are available. For more details, see
<arXiv:1506.02494>.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
