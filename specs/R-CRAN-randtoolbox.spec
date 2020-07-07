%global packname  randtoolbox
%global packver   1.30.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.30.1
Release:          3%{?dist}
Summary:          Toolbox for Pseudo and Quasi Random Number Generation and RandomGenerator Tests

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rngWELL >= 0.10.1
Requires:         R-CRAN-rngWELL >= 0.10.1

%description
Provides (1) pseudo random generators - general linear congruential
generators, multiple recursive generators and generalized feedback shift
register (SF-Mersenne Twister algorithm and WELL generators); (2) quasi
random generators - the Torus algorithm, the Sobol sequence, the Halton
sequence (including the Van der Corput sequence) and (3) some generator
tests - the gap test, the serial test, the poker test. See e.g. Gentle
(2003) <doi:10.1007/b97336>. The package can be provided without the
rngWELL dependency on demand. Take a look at the Distribution task view of
types and tests of random number generators. Version in Memoriam of
Diethelm and Barbara Wuertz.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
