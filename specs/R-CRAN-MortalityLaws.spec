%global packname  MortalityLaws
%global packver   1.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Parametric Mortality Models, Life Tables and HMD

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl >= 1.95
BuildRequires:    R-CRAN-pbapply >= 1.3.4
BuildRequires:    R-CRAN-minpack.lm >= 1.2
BuildRequires:    R-CRAN-tidyr >= 0.8.1
Requires:         R-CRAN-RCurl >= 1.95
Requires:         R-CRAN-pbapply >= 1.3.4
Requires:         R-CRAN-minpack.lm >= 1.2
Requires:         R-CRAN-tidyr >= 0.8.1

%description
Fit the most popular human mortality 'laws', and construct full and
abridge life tables given various input indices. A mortality law is a
parametric function that describes the dying-out process of individuals in
a population during a significant portion of their life spans. For a
comprehensive review of the most important mortality laws see Tabeau
(2001) <doi:10.1007/0-306-47562-6_1>. Practical functions for downloading
data from various human mortality databases are provided as well.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
