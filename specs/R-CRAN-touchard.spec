%global packname  touchard
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          2%{?dist}
Summary:          Touchard Model and Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-MASS 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-plotrix 

%description
Tools for analyzing count data with the Touchard model (Matsushita et al.,
2018, Comm Stat Th Meth <doi:10.1080/03610926.2018.1444177>). It includes
univariate estimation (ML and MM) and regression tools developed by
Andrade et al. (submitted).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
