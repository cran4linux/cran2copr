%global packname  frontier
%global packver   1.1-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.8
Release:          2%{?dist}
Summary:          Stochastic Frontier Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-stats >= 2.15.0
BuildRequires:    R-CRAN-plm >= 1.0.1
BuildRequires:    R-CRAN-lmtest >= 0.9.24
BuildRequires:    R-CRAN-micEcon >= 0.6.14
BuildRequires:    R-CRAN-miscTools >= 0.6.1
BuildRequires:    R-CRAN-Formula >= 0.2.0
BuildRequires:    R-CRAN-moments >= 0.11
Requires:         R-stats >= 2.15.0
Requires:         R-CRAN-plm >= 1.0.1
Requires:         R-CRAN-lmtest >= 0.9.24
Requires:         R-CRAN-micEcon >= 0.6.14
Requires:         R-CRAN-miscTools >= 0.6.1
Requires:         R-CRAN-Formula >= 0.2.0
Requires:         R-CRAN-moments >= 0.11

%description
Maximum Likelihood Estimation of Stochastic Frontier Production and Cost
Functions. Two specifications are available: the error components
specification with time-varying efficiencies (Battese and Coelli, 1992,
<doi:10.1007/BF00158774>) and a model specification in which the firm
effects are directly influenced by a number of variables (Battese and
Coelli, 1995, <doi:10.1007/BF01205442>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install
test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R && echo "FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch" > ~/.R/Makevars
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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/front41
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
