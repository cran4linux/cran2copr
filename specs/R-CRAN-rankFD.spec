%global packname  rankFD
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Rank-Based Tests for General Factorial Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.43
BuildRequires:    R-Matrix >= 1.2.2
BuildRequires:    R-CRAN-coin >= 1.1.2
BuildRequires:    R-lattice >= 0.20.33
Requires:         R-MASS >= 7.3.43
Requires:         R-Matrix >= 1.2.2
Requires:         R-CRAN-coin >= 1.1.2
Requires:         R-lattice >= 0.20.33

%description
The rankFD() function calculates the Wald-type statistic (WTS) and the
ANOVA-type statistic (ATS) for nonparametric factorial designs, e.g., for
count, ordinal or score data in a crossed design with an arbitrary number
of factors.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
