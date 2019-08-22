%global packname  calACS
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}
Summary:          Calculations for All Common Subsequences

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Implements several string comparison algorithms, including calACS (count
all common subsequences), lenACS (calculate the lengths of all common
subsequences), and lenLCS (calculate the length of the longest common
subsequence). Some algorithms differentiate between the more strict
definition of subsequence, where a common subsequence cannot be separated
by any other items, from its looser counterpart, where a common
subsequence can be interrupted by other items. This difference is shown in
the suffix of the algorithm (-Strict vs -Loose). For example, q-w is a
common subsequence of q-w-e-r and q-e-w-r on the looser definition, but
not on the more strict definition. calACSLoose Algorithm from Wang, H. All
common subsequences (2007) IJCAI International Joint Conference on
Artificial Intelligence, pp. 635-640.

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
%{rlibdir}/%{packname}/INDEX
