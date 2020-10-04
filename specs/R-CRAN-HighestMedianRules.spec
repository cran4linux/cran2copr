%global packname  HighestMedianRules
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation of Voting Rules Electing the Candidate withHighest Median Grade

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RMallow 
Requires:         R-CRAN-RMallow 

%description
Computes the scores and ranks candidates according to voting rules
electing the highest median grade. Based on "Tie-breaking the highest
median: alternatives to the majority judgment", A. Fabre, Social Choice &
Welfare (forthcoming as of 2020). The paper is available here:
<https://github.com/bixiou/highest_median/raw/master/Tie-breaking%20Highest%20Median%20-%20Fabre%202019.pdf>.
Functions to plot the voting profiles can be found on github:
<https://github.com/bixiou/highest_median/blob/master/packages_functions_data.R>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
