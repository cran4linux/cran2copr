%global __brp_check_rpaths %{nil}
%global packname  echo.find
%global packver   4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Finding Rhythms Using Extended Circadian Harmonic Oscillators(ECHO)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-boot >= 1.3.22
BuildRequires:    R-CRAN-minpack.lm >= 1.2.1
Requires:         R-boot >= 1.3.22
Requires:         R-CRAN-minpack.lm >= 1.2.1

%description
Provides a function (echo_find()) designed to find rhythms from data using
extended harmonic oscillators. For more information, see H. De los Santos
et al. (2020) <doi:10.1093/bioinformatics/btz617> .

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
%{rlibdir}/%{packname}
