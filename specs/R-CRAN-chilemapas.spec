%global __brp_check_rpaths %{nil}
%global packname  chilemapas
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Mapas de las Divisiones Politicas y Administrativas de Chile(Maps of the Political and Administrative Divisions of Chile)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-rmapshaper 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-rmapshaper 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 

%description
Mapas terrestres con topologias simplificadas. Estos mapas no tienen
precision geodesica, por lo que aplica el DFL-83 de 1979 de la Republica
de Chile y se consideran referenciales sin validez legal. No se incluyen
los territorios antarticos y bajo ningun evento estos mapas significan que
exista una cesion u ocupacion de territorios soberanos en contra del
Derecho Internacional por parte de Chile. Esta paquete esta documentado
intencionalmente en castellano asciificado para que funcione sin problema
en diferentes plataformas. (Terrestrial maps with simplified toplogies.
These maps lack geodesic precision, therefore DFL-83 1979 of the Republic
of Chile applies and are considered to have no legal validity. Antartic
territories are excluded and under no event these maps mean there is a
cession or occupation of sovereign territories against International Laws
from Chile. This package was intentionally documented in asciified spanish
to make it work without problem on different platforms.)

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
