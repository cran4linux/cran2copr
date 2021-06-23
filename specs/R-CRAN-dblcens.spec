%global __brp_check_rpaths %{nil}
%global packname  dblcens
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Compute the NPMLE of distribution from doubly censored data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0

%description
Use EM algorithm to compute the NPMLE of CDF and also the two censoring
distributions. For doubly censored data (as described in Chang and Yang
(1987) Ann. Stat. 1536-47). You can also specify a constraint, it will
return the constrained NPMLE and the -2 log empirical likelihood ratio.
This can be used to test the hypothesis about the constraint and find
confidence intervals for probability or quantile via empirical likelihood
ratio theorem. Influence function of hat F may also be calculated (but may
be slow).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
