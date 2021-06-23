%global __brp_check_rpaths %{nil}
%global packname  switchnpreg
%global packver   0.8-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          3%{?dist}%{?buildtag}
Summary:          Switching nonparametric regression models for a single curve andfunctional data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-HiddenMarkov 
Requires:         R-MASS 
Requires:         R-splines 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-HiddenMarkov 

%description
Functions for estimating the parameters from the latent state process and
the functions corresponding to the J states as proposed by De Souza and
Heckman (2013).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/demo-support-files
%{rlibdir}/%{packname}/INDEX
