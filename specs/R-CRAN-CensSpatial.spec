%global __brp_check_rpaths %{nil}
%global packname  CensSpatial
%global packver   2.58
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.58
Release:          2%{?dist}%{?buildtag}
Summary:          Censored Spatial Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 2.11.1
BuildRequires:    R-CRAN-tlrmvnmvt >= 1.1.0
BuildRequires:    R-CRAN-geoR 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-lattice 
Requires:         R-CRAN-numDeriv >= 2.11.1
Requires:         R-CRAN-tlrmvnmvt >= 1.1.0
Requires:         R-CRAN-geoR 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-moments 
Requires:         R-lattice 

%description
It fits linear regression models for censored spatial data. It provides
different estimation methods as the SAEM (Stochastic Approximation of
Expectation Maximization) algorithm and seminaive that uses Kriging
prediction to estimate the response at censored locations and predict new
values at unknown locations. It also offers graphical tools for assessing
the fitted model. More details can be found in Ordonez et al. (2018)
<doi:10.1016/j.spasta.2017.12.001>.

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
