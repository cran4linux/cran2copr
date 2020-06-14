%global packname  optweight
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          2%{?dist}
Summary:          Targeted Stable Balancing Weights Using Optimization

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-Matrix >= 1.2.13
BuildRequires:    R-CRAN-osqp >= 0.6.0.2
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-Matrix >= 1.2.13
Requires:         R-CRAN-osqp >= 0.6.0.2

%description
Use optimization to estimate weights that balance covariates for binary,
multinomial, and continuous treatments in the spirit of Zubizarreta (2015)
<doi:10.1080/01621459.2015.1023805>. The degree of balance can be
specified for each covariate. In addition, sampling weights can be
estimated that allow a sample to generalize to a population specified with
given target moments of covariates.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
