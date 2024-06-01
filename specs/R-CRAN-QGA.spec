%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QGA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quantum Genetic Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Function that implements the Quantum Genetic Algorithm, first proposed by
Han and Kim in 2000. This is an R implementation of the 'python'
application developed by Lahoz-Beltra
(<https://github.com/ResearchCodesHub/QuantumGeneticAlgorithms>). Each
optimization problem is represented as a maximization one, where each
solution is a sequence of (qu)bits. Following the quantum paradigm, these
qubits are in a superposition state: when measuring them, they collapse in
a 0 or 1 state. After measurement, the fitness of the solution is
calculated as in usual genetic algorithms. The evolution at each iteration
is oriented by the application of two quantum gates to the amplitudes of
the qubits: (1) a rotation gate (always); (2) a Pauli-X gate (optionally).
The rotation is based on the theta angle values: higher values allow a
quicker evolution, and lower values avoid local maxima. The Pauli-X gate
is equivalent to the classical mutation operator and determines the swap
between alfa and beta amplitudes of a given qubit. The package has been
developed in such a way as to permit a complete separation between the
engine, and the particular problem subject to combinatorial optimization.

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
