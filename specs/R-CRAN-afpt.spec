%global packname  afpt
%global packver   1.1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0.1
Release:          1%{?dist}
Summary:          Tools for Modelling of Animal Flight Performance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-stats 

%description
Allows estimation and modelling of flight costs in animal (vertebrate)
flight, implementing the aerodynamic power model described in Klein
Heerenbrink et al. (2015) <doi:10.1098/rspa.2014.0952>. Taking inspiration
from the program 'Flight', developed by Colin Pennycuick (Pennycuick
(2008) "Modelling the flying bird". Amsterdam: Elsevier. ISBN
0-19-857721-4), flight performance is estimated based on basic
morphological measurements such as body mass, wingspan and wing area.
'afpt' can be used to make predictions on how animals should adjust their
flight behaviour and wingbeat kinematics to varying flight conditions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
