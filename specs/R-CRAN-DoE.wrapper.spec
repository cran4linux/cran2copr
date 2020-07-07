%global packname  DoE.wrapper
%global packver   0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11
Release:          3%{?dist}
Summary:          Wrapper Package for Design of Experiments Functionality

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FrF2 >= 1.6
BuildRequires:    R-CRAN-AlgDesign >= 1.1
BuildRequires:    R-CRAN-DoE.base >= 0.23.4
BuildRequires:    R-CRAN-rsm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-DiceDesign 
Requires:         R-CRAN-FrF2 >= 1.6
Requires:         R-CRAN-AlgDesign >= 1.1
Requires:         R-CRAN-DoE.base >= 0.23.4
Requires:         R-CRAN-rsm 
Requires:         R-stats 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-DiceDesign 

%description
Various kinds of designs for (industrial) experiments can be created. The
package uses, and sometimes enhances, design generation routines from
other packages. So far, response surface designs from package rsm, latin
hypercube samples from packages lhs and DiceDesign, and D-optimal designs
from package AlgDesign have been implemented.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
