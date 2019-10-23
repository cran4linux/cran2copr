%global packname  LHD
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Latin Hypercube Designs (LHDs) Algorithms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Contains functions for finding space-filling Latin Hypercube Designs
(LHDs), e.g. maximin distance LHDs. Unlike other packages, our package is
particularly useful in the area of Design and Analysis of Experiments
(DAE). More specifically, it is very useful in design of computer
experiments. One advantage of our package is its comprehensiveness. It
contains a variety of heuristic algorithms (and their modifications) for
searching maximin distance LHDs. In addition to that, it also contains
other useful tools for developing and constructing maximin distance LHDs.
In the future, algebraic construction methods will be added. Please refer
to the function documentations for the detailed references of each
function. Among all the references we used, one reference should be
highlighted here, which is Ruichen Jin, Wei Chen, Agus Sudjianto (2005)
<doi:10.1016/j.jspi.2004.02.014>. They provided a new form of phi_p
criterion, which does not lose the space-filling property and
simultaneously reduces the computational complexity when evaluating (or
re-evaluating) an LHD. Their new phi_p criterion is a fundamental
component of our many functions. Besides, the computation nature of the
new phi_p criterion enables our functions to have less CPU time.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
