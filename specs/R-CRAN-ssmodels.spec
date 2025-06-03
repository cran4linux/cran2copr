%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssmodels
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Selection Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1.1
BuildRequires:    R-CRAN-Rdpack >= 2.4
BuildRequires:    R-CRAN-pracma >= 2.3.8
BuildRequires:    R-CRAN-sn >= 2.1.0
BuildRequires:    R-CRAN-miscTools >= 0.6.26
Requires:         R-CRAN-numDeriv >= 2016.8.1.1
Requires:         R-CRAN-Rdpack >= 2.4
Requires:         R-CRAN-pracma >= 2.3.8
Requires:         R-CRAN-sn >= 2.1.0
Requires:         R-CRAN-miscTools >= 0.6.26

%description
In order to facilitate the adjustment of the sample selection models
existing in the literature, we created the 'ssmodels' package. Our package
allows the adjustment of the classic Heckman model (Heckman (1976),
Heckman (1979) <doi:10.2307/1912352>), and the estimation of the
parameters of this model via the maximum likelihood method and two-step
method, in addition to the adjustment of the Heckman-t models introduced
in the literature by Marchenko and Genton (2012)
<doi:10.1080/01621459.2012.656011> and the Heckman-Skew model introduced
in the literature by Ogundimu and Hutton (2016) <doi:10.1111/sjos.12171>.
We also implemented functions to adjust the generalized version of the
Heckman model, introduced by Bastos, Barreto-Souza, and Genton (2021)
<doi:10.5705/ss.202021.0068>, that allows the inclusion of covariables to
the dispersion and correlation parameters, and a function to adjust the
Heckman-BS model introduced by Bastos and Barreto-Souza (2020)
<doi:10.1080/02664763.2020.1780570> that uses the Birnbaum-Saunders
distribution as a joint distribution of the selection and primary
regression variables. This package extends and complements existing R
packages such as 'sampleSelection' (Toomet and Henningsen, 2008) and
'ssmrob' (Zhelonkin et al., 2016), providing additional robust and
flexible sample selection models.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
