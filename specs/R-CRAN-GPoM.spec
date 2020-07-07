%global packname  GPoM
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          Generalized Polynomial Modelling

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-float 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-float 

%description
Platform dedicated to the Global Modelling technique. Its aim is to obtain
ordinary differential equations of polynomial form directly from time
series. It can be applied to single or multiple time series under various
conditions of noise, time series lengths, sampling, etc. This platform is
developped at the Centre d'Etudes Spatiales de la Biosphere (CESBIO), UMR
5126 UPS/CNRS/CNES/IRD, 18 av. Edouard Belin, 31401 TOULOUSE, FRANCE. The
developments were funded by the French program Les Enveloppes Fluides et
l'Environnement (LEFE, MANU, projets GloMo, SpatioGloMo and MoMu). The
French program Defi InFiNiTi (CNRS) and PNTS are also acknowledged
(projects Crops'IChaos and Musc & SlowFast).

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
