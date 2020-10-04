%global packname  BSS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Brownian Semistationary Processes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-phangorn 
Requires:         R-CRAN-hypergeo 
Requires:         R-MASS 
Requires:         R-CRAN-phangorn 

%description
Efficient simulation of Brownian semistationary (BSS) processes using the
hybrid simulation scheme, as described in Bennedsen, Lunde, Pakkannen
(2017) <arXiv:1507.03004v4>, as well as functions to fit BSS processes to
data, and functions to estimate the stochastic volatility process of a BSS
process.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
