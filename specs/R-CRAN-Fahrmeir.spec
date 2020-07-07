%global packname  Fahrmeir
%global packver   2016.5.31
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2016.5.31
Release:          3%{?dist}
Summary:          Data from the Book "Multivariate Statistical Modelling Based onGeneralized Linear Models", First Edition, by Ludwig Fahrmeirand Gerhard Tutz

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.1.0
Requires:         R-core >= 2.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Data and functions for the book "Multivariate Statistical Modelling Based
on Generalized Linear Models", first edition, by Ludwig Fahrmeir and
Gerhard Tutz.  Useful when using the book.

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
%{rlibdir}/%{packname}/INDEX
