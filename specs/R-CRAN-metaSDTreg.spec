%global packname  metaSDTreg
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Regression Models for Meta Signal Detection Theory

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.3
Requires:         R-core >= 3.4.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ordinal >= 2015.6.28
BuildRequires:    R-CRAN-maxLik >= 1.3.4
BuildRequires:    R-Matrix >= 1.2.17
BuildRequires:    R-CRAN-truncnorm >= 1.0.7
Requires:         R-CRAN-ordinal >= 2015.6.28
Requires:         R-CRAN-maxLik >= 1.3.4
Requires:         R-Matrix >= 1.2.17
Requires:         R-CRAN-truncnorm >= 1.0.7

%description
Regression methods for the meta-SDT model. The package implements methods
for cognitive experiments of meta cognition as described in Kristensen, S.
B., Sandberg, K., & Bibby, B. M. (2020). Regression methods for
metacognitive sensitivity. Journal of Mathematical Psychology, 94.
<doi:10.1016/j.jmp.2019.102297>.

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
