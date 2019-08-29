%global packname  ExpDes
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Experimental Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stargazer 
Requires:         R-CRAN-stargazer 

%description
Package for analysis of simple experimental designs (CRD, RBD and LSD),
experiments in double factorial schemes (in CRD and RBD), experiments in a
split plot in time schemes (in CRD and RBD), experiments in double
factorial schemes with an additional treatment (in CRD and RBD),
experiments in triple factorial scheme (in CRD and RBD) and experiments in
triple factorial schemes with an additional treatment (in CRD and RBD),
performing the analysis of variance and means comparison by fitting
regression models until the third power (quantitative treatments) or by a
multiple comparison test, Tukey test, test of Student-Newman-Keuls (SNK),
Scott-Knott, Duncan test, t test (LSD) and Bonferroni t test (protected
LSD)(qualitative treatments); residual analysis (Ferreira, Cavalcanti and
Nogueira, 2014) <doi:10.4236/am.2014.519280>.

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
