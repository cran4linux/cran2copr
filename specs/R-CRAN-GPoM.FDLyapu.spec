%global __brp_check_rpaths %{nil}
%global packname  GPoM.FDLyapu
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Lyapunov Exponents and Kaplan-Yorke Dimension

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-GPoM 
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-GPoM 
Requires:         R-CRAN-deSolve 

%description
Estimation of the spectrum of Lyapunov Exponents and the Kaplan-Yorke
dimension of any low-dimensional model of polynomial form. It can be
applied, for example, to systems such as the chaotic Lorenz-1963 system or
the hyperchaotic Rossler-1979 system. It can also be applied to dynamical
models in Ordinary Differential Equations (ODEs) directly obtained from
observational time series using the 'GPoM' package. The approach used is
semi-formal, the Jacobian matrix being estimated automatically from the
polynomial equations. Two methods are made available; one introduced by
Wolf et al. (1985) <doi:10.1016/0167-2789(85)90011-9> and the other one
introduced by Grond et al. (2003) <doi:10.1016/S0960-0779(02)00479-4>. The
package is provided with an interface for a more intuitive usage, it can
also be run without the interface. This platform is developed at the
Centre d'Etudes Spatiales de la Biosphere (CESBIO), UMR 5126
UPS/CNRS/CNES/IRD, 18 av. Edouard Belin, 31401 TOULOUSE, FRANCE. The
developments were funded by the French program Les Enveloppes Fluides et
l'Environnement (LEFE, MANU, projects GloMo, SpatioGloMo and MoMu). The
French programs Defi InFiNiTi (CNRS) and PNTS (CNRS) are also acknowledged
(projects Crops'I Chaos and Musc & SlowFast).

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny-examples
%{rlibdir}/%{packname}/INDEX
