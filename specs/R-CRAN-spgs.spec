%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spgs
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
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

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
