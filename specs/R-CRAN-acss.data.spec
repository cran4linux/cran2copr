%global __brp_check_rpaths %{nil}
%global packname  acss.data
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Data Only: Algorithmic Complexity of Short Strings (Computed viaCoding Theorem Method)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Data only package providing the algorithmic complexity of short strings,
computed using the coding theorem method. For a given set of symbols in a
string, all possible or a large number of random samples of Turing
machines (TM) with a given number of states (e.g., 5) and number of
symbols corresponding to the number of symbols in the strings were
simulated until they reached a halting state or failed to end. This
package contains data on 4.5 million strings from length 1 to 12 simulated
on TMs with 2, 4, 5, 6, and 9 symbols. The complexity of the string
corresponds to the distribution of the halting states of the TMs.

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
