%global packname  PUPAIM
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          A Collection of Physical and Chemical Adsorption Isotherm Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-minpack.lm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-nls2 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-minpack.lm 

%description
Adsorption isotherm equations are linearized plots of different
solid-liquid phase equilibria used in calculating different parameters
related to the adsorption process. Isotherm equations deals with physical
adsorption of gases and vapor and gives the most important characteristics
of industrial adsorbents that include pore volume, pore size or energy
distribution. PUPAIM has 28 documented adsorption isotherm models listed
by Dabrowski (2001) <doi:10.1016/S0001-8686(00)00082-8> and Ayawei et
al.(2017) <doi:10.1155/2017/3039817>. These models could be easily fitted
in R using adsorption data (Ce and Qe) obtained from experiments.

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
%{rlibdir}/%{packname}/INDEX
