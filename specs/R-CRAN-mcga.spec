%global packname  mcga
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          3%{?dist}
Summary:          Machine Coded Genetic Algorithms for Real-Valued OptimizationProblems

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
BuildRequires:    R-CRAN-GA 
Requires:         R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-GA 

%description
Machine coded genetic algorithm (MCGA) is a fast tool for real-valued
optimization problems. It uses the byte representation of variables rather
than real-values. It performs the classical crossover operations (uniform)
on these byte representations. Mutation operator is also similar to
classical mutation operator, which is to say, it changes a randomly
selected byte value of a chromosome by +1 or -1 with probability 1/2. In
MCGAs there is no need for encoding-decoding process and the classical
operators are directly applicable on real-values. It is fast and can
handle a wide range of a search space with high precision. Using a
256-unary alphabet is the main disadvantage of this algorithm but a
moderate size population is convenient for many problems. Package also
includes multi_mcga function for multi objective optimization problems.
This function sorts the chromosomes using their ranks calculated from the
non-dominated sorting algorithm.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
