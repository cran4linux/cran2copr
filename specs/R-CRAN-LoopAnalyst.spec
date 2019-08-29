%global packname  LoopAnalyst
%global packver   1.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}
Summary:          A Collection of Tools to Conduct Levins' Loop Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.8.0
Requires:         R-core >= 1.8.0
BuildArch:        noarch
BuildRequires:    R-nlme 
Requires:         R-nlme 

%description
Loop analysis makes qualitative predictions of variable change in a system
of causally interdependent variables, where "qualitative" means sign only
(i.e. increases, decreases, non change, and ambiguous). This
implementation includes output support for graphs in .dot file format for
use with visualization software such as 'graphviz'
(<http://graphviz.org>). 'LoopAnalyst' provides tools for the construction
and output of community matrices, computation and output of community
effect matrices, tables of correlations, adjoint, absolute feedback,
weighted feedback and weighted prediction matrices, change in life
expectancy matrices, and feedback, path and loop enumeration tools.

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
