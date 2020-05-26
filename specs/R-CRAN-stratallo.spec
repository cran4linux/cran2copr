%global packname  stratallo
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Optimum Sample Allocation in Stratified Random Sampling Scheme

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Functions in this package provide solution to classical problem in survey
methodology - an optimum sample allocation in stratified sampling scheme
with simple random sampling without replacement design in each stratum. In
this context, the optimal allocation is in the classical
Tschuprow-Neyman's sense, and it satisfies additional upper bounds
restrictions imposed on sample sizes in strata. There are four different
algorithms available to use, and one of them is Neyman optimal allocation
applied in a recursive way. All the algorithms are described in detail in
"Wojciak W. Optimal allocation in stratified sampling schemes. Master's
diploma thesis, Warsaw University of Technology. 2019", available on-line
at <http://home.elka.pw.edu.pl/~wwojciak/msc_optimal_allocation.pdf>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
