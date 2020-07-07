%global packname  epoc
%global packver   0.2.6-1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6.1.1
Release:          3%{?dist}
Summary:          Endogenous Perturbation Analysis of Cancer

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lassoshooting >= 0.1.4
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-survival 
Requires:         R-CRAN-lassoshooting >= 0.1.4
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-elasticnet 
Requires:         R-survival 

%description
Estimates sparse matrices A or G using fast lasso regression from mRNA
transcript levels Y and CNA profiles U. Two models are provided, EPoC A
where AY + U + R = 0 and EPoC G where Y = GU + E, the matrices R and E are
so far treated as noise. For details see the manual page of
'lassoshooting' and the article Rebecka Jörnsten, Tobias Abenius, Teresia
Kling, Linnéa Schmidt, Erik Johansson, Torbjörn E M Nordling, Bodil
Nordlander, Chris Sander, Peter Gennemark, Keiko Funa, Björn Nilsson,
Linda Lindahl, Sven Nelander (2011) <doi:10.1038/msb.2011.17>.

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
