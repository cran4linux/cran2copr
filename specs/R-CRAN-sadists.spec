%global packname  sadists
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Some Additional Distributions

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-PDQutils >= 0.1.1
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-orthopolynom 
Requires:         R-CRAN-PDQutils >= 0.1.1
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-orthopolynom 

%description
Provides the density, distribution, quantile and generation functions of
some obscure probability distributions, including the doubly non- central
t, F, Beta, and Eta distributions; the lambda-prime and K-prime; the
upsilon distribution; the (weighted) sum of non-central chi-squares to a
power; the (weighted) sum of log non-central chi-squares; the product of
non-central chi-squares to powers; the product of doubly non-central F
variables; the product of independent normals.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
