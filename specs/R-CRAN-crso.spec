%global __brp_check_rpaths %{nil}
%global packname  crso
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Cancer Rule Set Optimization ('crso')

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-stats 
Requires:         R-utils 

%description
An algorithm for identifying candidate driver combinations in cancer. CRSO
is based on a theoretical model of cancer in which a cancer rule is
defined to be a collection of two or more events (i.e., alterations) that
are minimally sufficient to cause cancer. A cancer rule set is a set of
cancer rules that collectively are assumed to account for all of ways to
cause cancer in the population. In CRSO every event is designated
explicitly as a passenger or driver within each patient. Each event is
associated with a patient-specific, event-specific passenger penalty,
reflecting how unlikely the event would have happened by chance, i.e., as
a passenger. CRSO evaluates each rule set by assigning all samples to a
rule in the rule set, or to the null rule, and then calculating the total
statistical penalty from all unassigned event. CRSO uses a three phase
procedure find the best rule set of fixed size K for a range of Ks. A core
rule set is then identified from among the best rule sets of size K as the
rule set that best balances rule set size and statistical penalty. Users
should consult the 'crso' vignette for an example walk through of a full
CRSO run. The full description, of the CRSO algorithm is presented in:
Klein MI, Cannataro V, Townsend J, Stern DF and Zhao H. "Identifying
combinations of cancer driver in individual patients." BioRxiv 674234
[Preprint]. June 19, 2019. <doi:10.1101/674234>. Please cite this article
if you use 'crso'.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
