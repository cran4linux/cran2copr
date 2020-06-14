%global packname  InfoTrad
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          2%{?dist}
Summary:          Calculates the Probability of Informed Trading (PIN)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-nloptr 
Requires:         R-CRAN-nloptr 

%description
Estimates the probability of informed trading (PIN) initially introduced
by Easley et. al. (1996) <doi:10.1111/j.1540-6261.1996.tb04074.x> .
Contribution of the package is that it uses likelihood factorizations of
Easley et. al. (2010) <doi:10.1017/S0022109010000074> (EHO factorization)
and Lin and Ke (2011) <doi:10.1016/j.finmar.2011.03.001> (LK
factorization). Moreover, the package uses different estimation
algorithms. Specifically, the grid-search algorithm proposed by Yan and
Zhang (2012) <doi:10.1016/j.jbankfin.2011.08.003> , hierarchical
agglomerative clustering approach proposed by Gan et. al. (2015)
<doi:10.1080/14697688.2015.1023336> and later extended by Ersan and Alici
(2016) <doi:10.1016/j.intfin.2016.04.001> .

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
