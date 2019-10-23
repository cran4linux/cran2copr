%global packname  NORTARA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Generation of Multivariate Data with Arbitrary Marginals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.7
BuildRequires:    R-Matrix >= 1.1.4
Requires:         R-CRAN-corpcor >= 1.6.7
Requires:         R-Matrix >= 1.1.4

%description
An implementation of a specific method for generating n-dimensional random
vectors with given marginal distributions and correlation matrix. The
method uses the NORTA (NORmal To Anything) approach which generates a
standard normal random vector and then transforms it into a random vector
with specified marginal distributions and the RA (Retrospective
Approximation) algorithm which is a generic stochastic root-finding
algorithm. The marginals can be continuous or discrete. See the vignette
of package for more details.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
