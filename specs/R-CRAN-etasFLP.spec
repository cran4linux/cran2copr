%global packname  etasFLP
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed FLP and ML Estimation of ETAS Space-Time Point Processesfor Earthquake Description

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-mapdata 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-maps 
Requires:         R-CRAN-mapdata 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-maps 

%description
Estimation of the components of an ETAS (Epidemic Type Aftershock
Sequence) model for earthquake description. Non-parametric background
seismicity can be estimated through FLP (Forward Likelihood Predictive).
New version 2.0.0: covariates have been introduced to explain the effects
of external factors on the induced seismicity; the parametrization has
been changed; Chiodi, Adelfio (2017)<doi:10.18637/jss.v076.i03>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
