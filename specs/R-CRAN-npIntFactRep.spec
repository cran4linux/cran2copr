%global packname  npIntFactRep
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Nonparametric Interaction Tests for Factorial Designs withRepeated Measures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ez 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-ez 
Requires:         R-CRAN-plyr 
Requires:         R-stats 

%description
Returns nonparametric aligned rank tests for the interaction in two-way
factorial designs, on R data sets with repeated measures in 'wide' format.
Five ANOVAs tables are reported. A PARAMETRIC one on the original data,
one for a CHECK upon the interaction alignments, and three aligned rank
tests: one on the aligned REGULAR, one on the FRIEDMAN, and one on the
KOCH ranks. In these rank tests, only the resulting values for the
interaction are relevant.

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
