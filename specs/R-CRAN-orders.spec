%global packname  orders
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Sampling from Order Statistics of New Families of Distributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Newdistns 
Requires:         R-CRAN-Newdistns 

%description
Set of tools to generate samples of order statistics from new families of
distributions. The main references for this package are: Gentle, J.
(2009), Computational Statistics, Springer-Verlag and Naradajah, S. and
Rocha, R. (2016),<DOI:10.18637/jss.v069.i10>. The families of
distributions are: Marshall Olkin G distributions, exponentiated G
distributions, beta G distributions, gamma G distributions, Kumaraswamy G
distributions, generalized beta G distributions, beta extended G
distributions, gamma G distributions, gamma uniform G distributions, beta
exponential G distributions, Weibull G distributions, log gamma G I
distributions, log gamma G II distributions, exponentiated generalized G
distributions, exponentiated Kumaraswamy G distributions, geometric
exponential Poisson G distributions, truncated-exponential skew-symmetric
G distributions, modified beta G distributions, and exponentiated
exponential Poisson G distributions.

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
