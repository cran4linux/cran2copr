%global packname  modehunt
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}%{?buildtag}
Summary:          Multiscale Analysis for Density Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Given independent and identically distributed observations X(1), ..., X(n)
from a density f, provides five methods to perform a multiscale analysis
about f as well as the necessary critical values. The first method,
introduced in Duembgen and Walther (2008), provides simultaneous
confidence statements for the existence and location of local increases
(or decreases) of f, based on all intervals I(all) spanned by any two
observations X(j), X(k). The second method approximates the latter
approach by using only a subset of I(all) and is therefore computationally
much more efficient, but asymptotically equivalent. Omitting the additive
correction term Gamma in either method offers another two approaches which
are more powerful on small scales and less powerful on large scales,
however, not asymptotically minimax optimal anymore. Finally, the block
procedure is a compromise between adding Gamma or not, having intermediate
power properties. The latter is again asymptotically equivalent to the
first and was introduced in Rufibach and Walther (2010).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
