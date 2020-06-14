%global packname  sigInt
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Estimate the Parameters of a Discrete Crisis-Bargaining Game

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-pbivnorm 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-MASS 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-pbivnorm 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-xtable 
Requires:         R-MASS 

%description
Provides pseudo-likelihood methods for empirically analyzing common
signaling games in international relations as described in Crisman-Cox and
Gibilisco (2019) <doi:10.1017/psrm.2019.58>.

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
