%global packname  lvnet
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Latent Variable Network Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-semPlot 
Requires:         R-CRAN-OpenMx 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-qgraph 
Requires:         R-Matrix 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-semPlot 

%description
Estimate, fit and compare Structural Equation Models (SEM) and network
models (Gaussian Graphical Models; GGM) using OpenMx. Allows for two
possible generalizations to include GGMs in SEM: GGMs can be used between
latent variables (latent network modeling; LNM) or between residuals
(residual network modeling; RNM). For details, see Epskamp, Rhemtulla and
Borsboom (2017) <doi:10.1007/s11336-017-9557-x>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
