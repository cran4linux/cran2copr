%global packname  spgs
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Statistical Patterns in Genomic Sequences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
A collection of statistical hypothesis tests and other techniques for
identifying certain spatial relationships/phenomena in DNA sequences. In
particular, it provides tests and graphical methods for determining
whether or not DNA sequences comply with Chargaff's second parity rule or
exhibit purine-pyrimidine parity. In addition, there are functions for
efficiently simulating discrete state space Markov chains and testing
arbitrary symbolic sequences of symbols for the presence of first-order
Markovianness. Also, it has functions for counting words/k-mers (and
cylinder patterns) in arbitrary symbolic sequences. Functions which take a
DNA sequence as input can handle sequences stored as SeqFastadna objects
from the 'seqinr' package.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
