%global __brp_check_rpaths %{nil}
%global packname  distTails
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          A Collection of Full Defined Distribution Tails

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ercv 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-MASS 
Requires:         R-CRAN-ercv 
Requires:         R-CRAN-gsl 
Requires:         R-MASS 

%description
A full definition for Weibull tails and Full-Tails Gamma and tools for
fitting these distributions to empirical tails. This package build upon
the paper by del Castillo, Joan & Daoudi, Jalila & Serra, Isabel. (2012)
<doi:10.1017/asb.2017.9>.

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
