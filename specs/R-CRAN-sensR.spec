%global packname  sensR
%global packver   1.5-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          3%{?dist}
Summary:          Thurstonian Models for Sensory Discrimination

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-numDeriv 
Requires:         R-CRAN-multcomp 
Requires:         R-MASS 
Requires:         R-CRAN-numDeriv 

%description
Provides methods for sensory discrimination methods; duotrio, tetrad,
triangle, 2-AFC, 3-AFC, A-not A, same-different, 2-AC and
degree-of-difference. This enables the calculation of d-primes, standard
errors of d-primes, sample size and power computations, and comparisons of
different d-primes. Methods for profile likelihood confidence intervals
and plotting are included.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
