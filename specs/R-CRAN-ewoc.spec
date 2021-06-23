%global __brp_check_rpaths %{nil}
%global packname  ewoc
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Escalation with Overdose Control

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-parallel >= 3.4.0
BuildRequires:    R-graphics >= 3.3.1
BuildRequires:    R-stats >= 3.3.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-doRNG >= 1.7.1
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-Formula >= 1.2.1
BuildRequires:    R-CRAN-doParallel >= 1.0.11
BuildRequires:    R-CRAN-coda >= 0.18.1
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-parallel >= 3.4.0
Requires:         R-graphics >= 3.3.1
Requires:         R-stats >= 3.3.1
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-doRNG >= 1.7.1
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-Formula >= 1.2.1
Requires:         R-CRAN-doParallel >= 1.0.11
Requires:         R-CRAN-coda >= 0.18.1

%description
An implementation of a variety of escalation with overdose control designs
introduced by Babb, Rogatko and Zacks (1998)
<doi:10.1002/(SICI)1097-0258(19980530)17:10%3C1103::AID-SIM793%3E3.0.CO;2-9>.
It calculates the next dose as a clinical trial proceeds and performs
simulations to obtain operating characteristics.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
