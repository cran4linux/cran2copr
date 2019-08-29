%global packname  concor
%global packver   1.0-0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}
Summary:          Concordance

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 0.99
Requires:         R-core >= 0.99
BuildArch:        noarch

%description
The four functions svdcp (cp for column partitioned), svdbip or svdbip2
(bip for bi-partitioned), and svdbips (s for a simultaneous optimization
of one set of r solutions), correspond to a "SVD by blocks" notion, by
supposing each block depending on relative subspaces, rather than on two
whole spaces as usual SVD does. The other functions, based on this notion,
are relative to two column partitioned data matrices x and y defining two
sets of subsets xi and yj of variables and amount to estimate a link
between xi and yj for the pair (xi, yj) relatively to the links associated
to all the other pairs.

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
