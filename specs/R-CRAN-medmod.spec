%global packname  medmod
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Simple Mediation and Moderation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-jmvcore >= 0.5.5
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-jmvcore >= 0.5.5
Requires:         R-CRAN-R6 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-ggplot2 

%description
This toolbox allows you to do simple mediation and moderation analysis. It
is also available as a module for 'jamovi' (see <https://www.jamovi.org>
for more information). 'Medmod' is based on the 'lavaan' package by Yves
Rosseel. You can find an in depth tutorial on the 'lavaan' model syntax
used for this package on <http://lavaan.ugent.be/tutorial/index.html>.

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
